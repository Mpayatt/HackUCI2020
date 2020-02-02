import firebase_admin
from flask import Flask, request, session
from firebase_admin import credentials
from firebase_admin import db, firestore
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import paralleldots
from tes2 import getContacts
from test import sentimentVal, messageSent

SECRET_KEY = 'a secret key'
api_key = '' #DO NOT PUBLISH KEY!
paralleldots.set_api_key(api_key)

app = Flask(__name__)
app.config.from_object(__name__)
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

cred = credentials.Certificate('./ServiceAccountKey.json') #COMMENT OUT IN GIT
#default_app = firebase_admin.initialize_app(cred)
caller = firestore.client()
phone_ref = caller.document(u'contactInfo/Test')

# Try adding your own number to this list!
callers = {
    "+14158675308": ["Rey", 1],
    "+12349013030": ["Finn", 3],
    "+12348134522": ["Chewy", 5],
}

username = ""
contacts_nums = []
users_num = 0
#user_progress = 0


@app.route('/bot', methods=['GET', 'POST'])
def bot():
    counter = session.get('counter', 0)
    counter += 1
    from_number = request.values.get('From')
    
    if from_number in callers:
        name = callers[from_number][0]
        progress = callers[from_number][1]
    else:
        name = "Friend"
        callers[from_number] = ["Friend", 0]
        progress = 0

    # State 0: Ask for Name
    if progress == 0:
        message = "What's your name friend?"
        callers[from_number][1] += 1
    # State 1: Get phone numbers
    elif progress == 1:
        incoming_msg = request.values.get('Body', '')
        callers[from_number][0] = incoming_msg
        callers[from_number][1] += 1
        message = "Hello {}, could you give your first contact number?".format(callers[from_number][0])
    # State 2: Receieve numbers
    elif progress == 2:
        incoming_msg = request.values.get('Body', '').lower()

        # If message is stop, stop sending numbers
        if incoming_msg == "done":
            callers[from_number][1] += 1
            message = "All set"
        else:
            callers[from_number].append(incoming_msg)
        #callers[from_number][1] += 1
            message = "{} has been entered. Say 'done' when you are done".format(incoming_msg)
    else:
        message = '{} has messaged {} {} times.' \
        .format(name, request.values.get('To'), counter)

    resp = MessagingResponse()
    resp.message(message)


    session['counter'] = counter

    return str(resp)

def senderBot():
    from_number = request.values.get('From')        #acquires phone number
    name, contacts = getContacts(from_number)       #gets victim's name and emergency contacts
    incoming_msg = request.values.get('Body', '').lower()   #text message they sent
    emotion = sentimentVal(incoming_msg)                #sentiment analysis
    response = messageSent(incoming_mesg, emotion, name)
    for person in contacts:                         #Loop to send the message
        message = client.messages.create(
            body = response,
            from_ = 'XXXXXXXXXX',
            to = person
            )
        print(message.sid)


app.run(debug=True)
