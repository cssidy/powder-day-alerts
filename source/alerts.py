#! /usr/bin/python3.5
# sends texts with Twilio

import scraper
from twilio.rest import Client


def send_text():
    if element >= 6:

        # send text with Twilio
        account_sid = ""
        auth_token = ""
        client = Client(account_sid, auth_token)

        client.api.account.messages.create(

            to="",
            from_="",
            body=("It snowed " + element + 'inches at %s in the past 24 hours.' % (mountain))
        )

        print('Just sent a text message...')
    else:
        pass

send_text()

