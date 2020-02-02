import firebase_admin
from firebase_admin import credentials
from firebase_admin import db, firestore
from twilio.rest import Client
from flask import Flask, request, session
import requests
from twilio.twiml.messaging_response import MessagingResponse

cred = credentials.Certificate('./ServiceAccountKey.json') #COMMENT OUT IN GIT
default_app = firebase_admin.initialize_app(cred)
caller = firestore.client()
phone_ref = caller.document(u'contactInfo/Test')


def quickstart_new_instance():
    db = firestore.client()

    return db


def quickstart_add_data_one():
    db = firestore.client()
    
    doc_ref = db.document(u'Test')
    doc_ref.set({
        u'Name': u'Jeff',
        u'Progress': 0,
        u'Contacts': [8058619283, 8053235430],
        u'UserNum': u'8058619283'
        })

def tryThisShit(phone_ref):
    db = firestore.client()
    doc_ref = db.collection(u'contactInfo').document(u'Test')
    try:
        doc = doc_ref.get()
        print(u'Document data: {}'.format(doc.to_dict()))
    except google.cloud.exceptions.NotFound:
        print(u'No such document!')
    contacts = phone_ref.get().to_dict()["PhoneNum"]["Contacts"]
    name = phone_ref.get().to_dict()["PhoneNum"]["Name"]
    print(name, contacts)



tryThisShit(phone_ref)
