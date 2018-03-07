#! /usr/bin/python3.5
# scrapes google search engine for current snow reports

import bs4
import requests
from twilio.rest import Client

mountain_list = ['Stowe+Mountain+Resort',
                 'Smugglers+Notch',
                 'Killington+Ski+Resort',
                 'Jay+Peak+Resort',
                 'Burke+Mountain+Ski+Area',
                 'Bolton+Valley+Ski+Area',
                 'Sugarbush+Resort',
                 'Mad+River+Glen']


def scraper():
    for mountain in mountain_list:

        print('Downloading current snow report for %s...' % (mountain))

        # get page
        res = requests.get('https://www.google.com/search?ei=JiOgWtGbBIeSsAWZmpvAAg&q=%+snow+report' % (mountain))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # get current snow report for last 24 hours
        print('Searching for recent snowfall at %s...' % (mountain))
        element = soup.find_all(text="24 Hours")
        # element = element[15]
        print(element)
        print('\n')

        '''


        if not element:
            print('Could not find recent snow fall for %s.' % (mountain))
        else:
            print('Snowfall: ' + element)

            '''

        '''
        def send_text():
            if element >= 6:

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
        '''




scraper()
