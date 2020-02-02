from flask import Flask, request, session
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import paralleldots
from twilio.rest import Client
from user import User
from access_db import *
import google.cloud.exceptions

SECRET_KEY = 'a secret key'
api_key = '' #DO NOT PUBLISH KEY!
paralleldots.set_api_key(api_key)

app = Flask(__name__)
app.config.from_object(__name__)

### REMOVE THIS AT THE END ####
from keys import *

client = Client(account_sid, auth_token)

def is_valid_number(number):
    try:
        response = client.lookups.phone_numbers(number).fetch(type="carrier")
        return True
    except TwilioRestException as e:
        if e.code == 20404:
            return False
        else:
            raise e

@app.route('/bot', methods=['GET', 'POST'])
def bot():
    counter = session.get('counter', 0)
    counter += 1
    from_number = request.values.get('From')
    
    try:
        #retrieve this user
        current_user = getUser(from_number)
    except google.cloud.exceptions.NotFound:
        #user doesn't exist yet
        current_user = User("Friend", from_number, 0, [])
        write_data(current_user)
    except TypeError:
        current_user = User("Friend", from_number, 0, [])
        write_data(current_user)

    progress = current_user.getProgress()
    # State 0: Ask for Name
    if progress == 0:
        message = "What's your name friend?"
        current_user.setProgress(current_user.getProgress() + 1)
    # State 1: Get phone numbers
    elif progress == 1:
        incoming_msg = request.values.get('Body', '')
        current_user.setName(incoming_msg)
        current_user.setProgress(current_user.getProgress() + 1)
        message = "Hello {}, could you give your first contact number?".format(current_user.getName())
    # State 2: Receieve numbers
    elif progress == 2:
        incoming_msg = request.values.get('Body', '').lower()
        # If message is stop, stop sending numbers
        if incoming_msg == "done":
            current_user.setProgress(current_user.getProgress() + 1)
            message = "All set"
        else:
            # Checks if phone number is valid
            if is_valid_number(current_user.getPhoneNumber()):
                current_user.addContact(incoming_msg)
                message = "{} has been entered. Say 'done' when you are done".format(incoming_msg)
            else:
                message = "{} is a invalid phone number. Enter another one".format(incoming_msg)
    else:
        incoming_msg = request.values.get('Body', '')
        message = "Message sent to " + str(senderBot(current_user.getName(), current_user.getContacts(),incoming_msg))
    
    write_data(current_user) #update this user's state in the database

    resp = MessagingResponse()
    resp.message(message)


    session['counter'] = counter

    return str(resp)

def senderBot(name, contacts, msg):
    from_number = request.values.get('From')        #acquires phone number     #gets victim's name and emergency contacts
    incoming_msg = request.values.get('Body', '').lower()   #text message they sent
    #sentimentVal(incoming_msg)  
    
    response = name + " is okay. Sent message: " + msg + " -Mr Gency Bot"#messageSent(emotion, name)
    for person in contacts:                         #Loop to send the message
        message = client.messages.create(
            body = response,
            from_ = 'XXXXXXXXXX', #number hidden
            to = person
            )
        print(message.sid)
    return contacts


app.run(debug=True)
