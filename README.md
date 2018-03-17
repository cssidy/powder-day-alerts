# Powder Day Alerts
A script that watches Smugglers' Notch Resort for "powder days", sends alerts when 
more than 6" of snow has fallen in 24 hours.

### What's a powder day?
The best feeling in the world! Floating on a cloud of deep, white fluff, surfing the mountain, huge
flakes falling down, sprays of snow on every turn. It's what skiers and snowboarders dream of. And you
want to get it first, before every one else does.

### Hence I wrote a script 
This script will text you if it's a powder day as soon as a snow report is released.

### How to use
You must download this repository to your own machine, adjust the Twilio API credentials 
to match your own account's, adjust the phone number to match your own, and then create a 
Cron job for the powder.py script.

#### Cron instructions
Smugglers' Notch releases their snow report every day (during the open season) between 6am - 8am. Lifts 
open at 8:30am. I run the script everyday at 7:30am because it takes me an hour to get to the mountain.