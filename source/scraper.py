#! /usr/bin/python3.5
# scrapes google search engine for current snow reports

import bs4
import requests
import datetime
from twilio.rest import Client

'''
mountain_list = ['Stowe+Mountain+Resort',
                 'Smugglers+Notch',
                 'Killington+Ski+Resort',
                 'Jay+Peak+Resort',
                 'Burke+Mountain+Ski+Area',
                 'Bolton+Valley+Ski+Area',
                 'Sugarbush+Resort',
                 'Mad+River+Glen']
'''


def scraper():
    today = datetime.datetime.now()
    print('Downloading current snow report for %s...' % (today))

    # get page
    res = requests.get('https://www.smuggs.com/pages/winter/snowReport/')
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # get current snow report for last 24 hours
    print('Searching for recent snowfall at Smugg\'s...')
    element = soup.find_all('b')
    element = element[6].text
    print(element)
    print('\n')

    # if no element found
    if not element:
        print('Could not find recent snow fall data.')
    else:
        print('Snowfall: ' + element)

    snow_fall = int(element[0])

    # if element greater than 4 inches, it's a powder day
    if snow_fall >= 4:
        powder_day = True
    else:
        powder_day = False

    print(powder_day)

    def send_text():

        if powder_day:

            # send text with Twilio
            account_sid = "YOUR_ACCOUNT_SID"
            auth_token = "YOUR_AUTH_TOKEN"
            client = Client(account_sid, auth_token)

            client.api.account.messages.create(

                to="YOUR_PHONE",
                    from_="YOUR_TWILIO_NUMBER",
                    body=("It snowed " + element + 'inches at %s in the past 24 hours.' % (mountain))
                )

            print('Just sent a text message...')
        else:
            pass

    send_text()
    




scraper()
