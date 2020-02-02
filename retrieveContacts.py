import firebase_admin
from firebase_admin import credentials
from firebase_admin import db, firestore
from twilio.rest import Client
from flask import Flask, request, session
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client


def getContacts(phone_ref):
    contacts = phone_ref.get().to_dict()["PhoneNum"]["Contacts"]
    name = phone_ref.get().to_dict()["PhoneNum"]["Name"]
    return name, contacts    


