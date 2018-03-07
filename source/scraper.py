#! /usr/bin/python3.5
# scrapes google search engine for current snow reports

import bs4
import requests
import datetime

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

        soup = bs4.BeautifulSoup(res.text, "lxml")

        # get current snow report for last 24 hours
        print('Searching for recent snowfall at %s...' % (mountain))
        element = soup.select('#resultStats')
        element = element[0].text
        print(element)

        now = datetime.datetime.now()

        if element == []:
            print('Could not find recent snow fall for %s.' % (mountain))
        else:
            print('Snowfall: ' + element)


scraper()
