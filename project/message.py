from aiohttp import request
from twilio.rest import Client
from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse

account_sid = "AC115c1585970f4ecafae7b8b9c440d22b"
account_token = "e82fda8320c5b8a45a1070556f08a15c"

client = Client(account_sid, account_token)


def sendMessage(text):
    message = client.messages.create(
        body=text,
        from_='+18446781351',  # Your Twilio phone number
        to='+16032757875'  # Your phone number
    )

# go to verified called IDs and add moms number
