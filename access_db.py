import firebase_admin
from firebase_admin import credentials
from firebase_admin import db, firestore
from twilio.rest import Client
from flask import Flask, request, session
import requests
from twilio.twiml.messaging_response import MessagingResponse
from user import User

cred = credentials.Certificate('./ServiceAccountKey.json') #COMMENT OUT IN GIT
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()


def write_data(user):
    doc_ref = db.collection(u'contactInfo').document(user.getPhoneNumber())
    doc_ref.set({
        u'PhoneNum':    {"Contacts": user.getContacts(),
                         "Name" : user.getName(),
                         "Progress" : user.getProgress(),
                         "UserNum" : user.getPhoneNumber() }
        })

def getUser(phone_ref):
    #contacts = phone_ref.get().to_dict()["PhoneNum"]["Contacts"]
    #name = phone_ref.get().to_dict()["PhoneNum"]["Name"]
    #phonenum = phone_ref.get().to_dict()["PhoneNum"]["UserNum"]
    #progress = phone_ref.get().to_dict()["PhoneNum"]["Progress"]
    doc_ref = db.collection(u'contactInfo').document(phone_ref)
    return User(doc_ref.get().to_dict()["PhoneNum"]["Name"],
                doc_ref.get().to_dict()["PhoneNum"]["UserNum"],
                doc_ref.get().to_dict()["PhoneNum"]["Progress"],
                doc_ref.get().to_dict()["PhoneNum"]["Contacts"])

def getProgress(phone_ref):
    return phone_ref.get().to_dict()["PhoneNum"]["Progress"]