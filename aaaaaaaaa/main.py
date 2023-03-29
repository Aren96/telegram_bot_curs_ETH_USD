import time

import requests
from bs4 import BeautifulSoup
import datetime
from z import URL , Headers,chat_id ,TOKEN
from notifiers import get_notifier

# "the code allows you to monitor the ETH exchange rate against the dollar exchange rate through google search parsing

def get_procent():
    url = URL  # "https://www.google.com/search?q=eth+usd&oq=eth&aqs=chrome.0.69i59l4j69i60l4.1712j1j7&sourceid=chrome&ie=UTF-8"
    headers = Headers # your  'User-Agent':  you need to hit google "my user agent" and you will get the value that you need to insert here

    full_page = requests.get(url, headers=headers).text

    soup = BeautifulSoup(full_page, 'html.parser')

    convert_1 = soup.findAll("span", {"jsname": "SwWl3d"})   # parsing google by value

    convert = soup.findAll("span", {'jsname': "rfaVEf"})
    convert_1 = convert_1[0].text
    result = convert[0].text
    result = result.replace('(', '').replace(')', '')


    for i in convert_1:
        if i == '+':
            result = '+' + result
        elif i == '-':
            result = '-' + result


    return result



def tel():

    while True:

        time.sleep(3600)     # I wrote here so that every 60 minutes the program worked
                                # first message will be in 60 minutes
                                    # you can insert any value into time.sleep , unit is a second

        telegram = get_notifier('telegram')

        telegram.notify(token=TOKEN,chat_id=chat_id,message = get_procent())     #   in telegram you can find out your chat id and paste it here so that the program sends you a message


tel()