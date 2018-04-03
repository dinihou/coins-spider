import json
import os
import datetime
import requests
import threading
import difflib
import traceback
from colorama import init, Fore, Back, Style
init()

import logging
logging.basicConfig(filename=os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'pycoins.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

from playsound import playsound

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


class Utils:
    def ex_print(self, msg, foreground="black", background="white"):
        fground = foreground.upper()
        bground = background.upper()
        style = getattr(Fore, fground) + getattr(Back, bground)
        return style + msg + Style.BRIGHT + Style.RESET_ALL

    def str_diff (self, before, after):
        output = list(difflib.Differ().compare(before, after))
        return output

    def display_diff (self, diff_list):
        for item in diff_list:
            if item[0] == '+':
                print(self.ex_print('[add]' + item[2:], 'green') + '\n')
            elif item[0] == '-':
                print(self.ex_print('[rem]' + item[2:], 'red') + '\n')


class BinanceIntro(threading.Thread):
    def __init__(self, link):
        super(BinanceIntro, self).__init__()
        self.link = link
        self.stop_event = threading.Event()
        self.old_list = {}

    def play(self, loop=True):
        while True:
            playsound(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'notification.wav')
            if not loop:
                break

    def stop(self):
        self.stop_event.set()

    def stopped(self):
        return self.stop_event.is_set()

    def display(self):
        if not self.old_list:
            print('Display not ready ... try again later' + "\n")
        else:
            print('Binance Intro List : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            for list in self.old_list['list']:
                print(list)

    def diffrence (self, old, new):
        diff_list = Utils().str_diff (old, new)
        if diff_list:
            print('Binance Intro List Detecte : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            Utils().display_diff (diff_list)

    def run(self):
        new_list = {}
        while not self.stopped() and self.is_alive():
            try:
                page = requests.get(self.link)
                html = page.content
                parsed_html = BeautifulSoup(html, 'html.parser')
                if not self.old_list:
                    self.old_list['list'] = [item.text for item in
                                             parsed_html.body.find_all('li', attrs={'class': 'article-list-item'})]
                    self.old_list['date'] = datetime.datetime.now()
                else:
                    new_list['list'] = [item.text for item in parsed_html.body.find_all('li', attrs={'class': 'article-list-item'})]
                    self.old_list['date'], new_list['date'] = datetime.datetime.now(), datetime.datetime.now()
                    if self.old_list['list'] != new_list['list']:
                        try :
                            self.diffrence (self.old_list['list'], new_list['list'])
                        finally:
                             self.old_list['list'] = new_list['list']
                             self.play()

            except Exception as err:
                logger.error(err)
                logger.exception("message")
            self.stop_event.wait(15)


class BinanceNews(threading.Thread):
    def __init__(self, link):
        super(BinanceNews, self).__init__()
        self.link = link
        self.stop_event = threading.Event()
        self.old_list = {}

    def play(self, loop=True):
        while True:
            playsound(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'notification.wav')
            if not loop:
                break

    def stop(self):
        self.stop_event.set()

    def stopped(self):
        return self.stop_event.is_set()

    def display(self):
        if not self.old_list:
            print('Display not ready ... try again later' + "\n")
        else:
            print('Binance News List : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            for list in self.old_list['list']:
                print(list)

    def diffrence(self, old, new):
        print('Binance News List Detected : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
        diff_list = Utils().str_diff(old, new)
        if diff_list:
            Utils().display_diff(diff_list)

    def run(self):
        new_list = {}
        while not self.stopped() and self.is_alive():
            try:
                page = requests.get(self.link)
                html = page.content
                parsed_html = BeautifulSoup(html, 'html.parser')
                if not self.old_list:
                    self.old_list['list'] = [item.text for item in parsed_html.body.find_all('li', attrs={'class': 'article-list-item'})]
                    self.old_list['date'] = datetime.datetime.now()
                else:
                    new_list['list'] = [item.text for item in parsed_html.body.find_all('li', attrs={'class': 'article-list-item'})]
                    self.old_list['date'], new_list['date'] = datetime.datetime.now(), datetime.datetime.now()
                    if self.old_list['list'] != new_list['list']:
                        try:
                            self.diffrence(self.old_list['list'], new_list['list'])
                        finally:
                            self.old_list['list'] = new_list['list']
                            self.play()
            except Exception as err:
                logger.error(err)
                logger.exception("message")
            self.stop_event.wait(15)

class  BinanceAPI(threading.Thread):
    def __init__(self, link):
        super(BinanceAPI, self).__init__()
        self.link = link
        self.stop_event = threading.Event()
        self.old_list = {}

    def play(self, loop=True):
        while True:
            playsound(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'notification.wav')
            if not loop:
                break

    def stop(self):
        self.stop_event.set()

    def stopped(self):
        return self.stop_event.is_set()

    def display(self):
        if not self.old_list:
            print('Display not ready ... try again later' + "\n")
        else:
            print('Binance API List : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            for list in self.old_list['list']:
                print(list)

    def diffrence(self, old, new):

        diff_list = Utils().str_diff(old, new)
        if diff_list:
            print('Binance API List Detected : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            Utils().display_diff(diff_list)

    def run(self):
        new_list = {}
        while not self.stopped() and self.is_alive():
            try:
                page = requests.get(self.link)
                apiJSON = json.loads(page.content)
                if not self.old_list:
                    self.old_list['list'] = [item['baseAssetName'] + ' [' + item['symbol'] + ']' for item in apiJSON['data']]
                    self.old_list['date'] = datetime.datetime.now()
                else:
                    new_list['list'] = [item['baseAssetName'] + ' [' + item['symbol'] + ']' for item in apiJSON['data']]
                    self.old_list['date'], new_list['date'] = datetime.datetime.now(), datetime.datetime.now()
                    if self.old_list['list'] != new_list['list']:
                        try:
                            self.diffrence(self.old_list['list'], new_list['list'])
                        finally:
                            self.old_list['list'] = new_list['list']
                            self.play()

            except Exception as err:
                logger.error(err)
                logger.exception("message")
            self.stop_event.wait(15)

class OKexIntro(threading.Thread):
    def __init__(self, link):
        super(OKexIntro, self).__init__()
        self.link = link
        self.stop_event = threading.Event()
        self.old_list = {}

    def play(self, loop=True):
        while True:
            playsound(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'notification.wav')
            if not loop:
                break

    def stop(self):
        self.stop_event.set()

    def stopped(self):
        return self.stop_event.is_set()

    def display(self):
        if not self.old_list:
            print('Display not ready ... try again later' + "\n")
        else:
            print('OKex Intro List : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            for list in self.old_list['list']:
                print(list)

    def diffrence(self, old, new):
        diff_list = Utils().str_diff(old, new)
        if diff_list:
            print('OKex Intro List Deteced : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            Utils().display_diff(diff_list)

    def run(self):
        new_list = {}
        while not self.stopped() and self.is_alive():
            try:
                page = requests.get(self.link)
                html = page.content
                parsed_html = BeautifulSoup(html, 'html.parser')
                if not self.old_list:
                    self.old_list['list'] = [item.text for item in
                                             parsed_html.body.find_all('li', attrs={'class': 'article-list-item'})]
                    self.old_list['date'] = datetime.datetime.now()
                else:
                    new_list['list'] = [item.text for item in
                                        parsed_html.body.find_all('li', attrs={'class': 'article-list-item'})]
                    self.old_list['date'], new_list['date'] = datetime.datetime.now(), datetime.datetime.now()
                    if self.old_list['list'] != new_list['list']:
                        try:
                            self.diffrence(self.old_list['list'], new_list['list'])
                        finally:
                            self.old_list['list'] = new_list['list']
                            self.play()

            except Exception as err:
                logger.error(err)
                logger.exception("message")
            self.stop_event.wait(15)


class OKexNews(threading.Thread):
    def __init__(self, link):
        super(OKexNews, self).__init__()
        self.link = link
        self.stop_event = threading.Event()
        self.old_list = {}

    def play(self, loop=True):
        while True:
            playsound(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'notification.wav')
            if not loop:
                break

    def stop(self):
        self.stop_event.set()

    def stopped(self):
        return self.stop_event.is_set()

    def display(self):
        if not self.old_list:
            print('Display not ready ... try again later' + "\n")
        else:
            print('OKex News List : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            for list in self.old_list['list']:
                print(list)

    def diffrence(self, old, new):
        diff_list = Utils().str_diff(old, new)
        if diff_list:
            print('OKex News List Detected : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            Utils().display_diff(diff_list)

    def run(self):
        new_list = {}
        while not self.stopped() and self.is_alive():
            try:
                page = requests.get(self.link)
                html = page.content
                parsed_html = BeautifulSoup(html, 'html.parser')
                if not self.old_list:
                    self.old_list['list'] = [item.text for item in parsed_html.body.find_all('li', attrs={'class': 'article-list-item'})]
                    self.old_list['date'] = datetime.datetime.now()
                else:
                    new_list['list'] = [item.text for item in parsed_html.body.find_all('li', attrs={'class': 'article-list-item'})]
                    self.old_list['date'], new_list['date'] = datetime.datetime.now(), datetime.datetime.now()
                    if self.old_list['list'] != new_list['list']:
                        try:
                            self.diffrence(self.old_list['list'], new_list['list'])
                        finally:
                            self.old_list['list'] = new_list['list']
                            self.play()
            except Exception as err:
                logger.error(err)
                logger.exception("message")
            self.stop_event.wait(15)


class BitfinexTokens(threading.Thread):
    def __init__(self, link):
        super(BitfinexTokens, self).__init__()
        self.link = link
        self.stop_event = threading.Event()
        self.old_list = {}

    def play(self, loop=True):
        while True:
            playsound(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'notification.wav')
            if not loop:
                break

    def stop(self):
        self.stop_event.set()

    def stopped(self):
        return self.stop_event.is_set()

    def display(self):
        if not self.old_list:
            print('Display not ready ... try again later' + "\n")
        else:
            print('Bitfinex Tokens List : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            for list in self.old_list['list']:
                print(list)

    def diffrence(self, old, new):
        diff_list = Utils().str_diff(old, new)
        if diff_list:
            print('Bitfinex Tokens List Detected: ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            Utils().display_diff(diff_list)

    def run(self):
        new_list = {}
        while not self.stopped() and self.is_alive():
            try:
                page = requests.get(self.link)
                html = page.content
                parsed_html = BeautifulSoup(html, 'html.parser')
                if not self.old_list:
                    self.old_list['list'] = [item.text for item in parsed_html.body.find_all('li', attrs={'class': 'article-list-item'})]
                    self.old_list['date'] = datetime.datetime.now()
                else:
                    new_list['list'] = [item.text for item in parsed_html.body.find_all('li', attrs={'class': 'article-list-item'})]
                    self.old_list['date'], new_list['date'] = datetime.datetime.now(), datetime.datetime.now()
                    if self.old_list['list'] != new_list['list']:
                        try:
                            self.diffrence(self.old_list['list'], new_list['list'])
                        finally:
                            self.old_list['list'] = new_list['list']
                            self.play()
            except Exception as err:
                logger.error(err)
                logger.exception("message")
            self.stop_event.wait(15)


class HuobiAPINotice(threading.Thread):
    def __init__(self, link):
        super(HuobiAPINotice, self).__init__()
        self.link = link
        self.stop_event = threading.Event()
        self.old_list = {}

    def play(self, loop=True):
        while True:
            playsound(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'notification.wav')
            if not loop:
                break

    def stop(self):
        self.stop_event.set()

    def stopped(self):
        return self.stop_event.is_set()

    def display(self):
        if not self.old_list:
            print('Display not ready ... try agin later' + "\n")
        else:
            print('Huobi Notice List : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            for list in self.old_list['list']:
                print(list)

    def diffrence(self, old, new):
        diff_list = Utils().str_diff(old, new)
        if diff_list:
            print('Huobi Notice List Detected : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            Utils().display_diff(diff_list)

    def run(self):
        new_list = {}
        while not self.stopped():
            try:
                page = requests.get(self.link)
                apiJSON = json.loads(page.content)
                if not self.old_list:
                    self.old_list['list'] = [item['title'] for item in apiJSON['data']['items']]
                    self.old_list['date'] = datetime.datetime.now()
                else:
                    new_list['list'] = [item['title'] for item in apiJSON['data']['items']]
                    self.old_list['date'], new_list['date'] = datetime.datetime.now(), datetime.datetime.now()
                    if self.old_list['list'] != new_list['list']:
                        try:
                            self.diffrence(self.old_list['list'], new_list['list'])
                        finally:
                            self.old_list['list'] = new_list['list']
                            self.play()
            except Exception as err:
                logger.error(err)
                logger.exception("message")
            self.stop_event.wait(15)


class HuobiAPINews(threading.Thread):
    def __init__(self, link):
        super(HuobiAPINews, self).__init__()
        self.link = link
        self.stop_event = threading.Event()
        self.old_list = {}

    def play(self, loop=True):
        while True:
            playsound(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'notification.wav')
            if not loop:
                break

    def stop(self):
        self.stop_event.set()

    def stopped(self):
        return self.stop_event.is_set()

    def display(self):
        if not self.old_list:
            print('Display not ready ... try again later' + "\n")
        else:
            print('Huobi News List : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            for list in self.old_list['list']:
                print(list)

    def diffrence (self, old, new):
        diff_list = Utils().str_diff(old, new)
        if diff_list:
            print('Huobi News List Detected : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            Utils().display_diff(diff_list)

    def run(self):
        new_list = {}
        while not self.stopped() and self.is_alive():
            try:
                page = requests.get(self.link)
                apiJSON = json.loads(page.content)
                if not self.old_list:
                    self.old_list['list'] = [item['pageIdentifier'] + ' [' + item['title'] + ']' for item in apiJSON['data']]
                    self.old_list['date'] = datetime.datetime.now()
                else:
                    new_list['list'] = [item['pageIdentifier'] + ' [' + item['title'] + ']' for item in apiJSON['data']]
                    self.old_list['date'], new_list['date'] = datetime.datetime.now(), datetime.datetime.now()
                    if self.old_list['list'] != new_list['list']:
                        try:
                            self.diffrence(self.old_list['list'], new_list['list'])
                        finally:
                            self.old_list['list'] = new_list['list']
                            self.play()
            except Exception as err:
                logger.error(err)
                logger.exception("message")
            self.stop_event.wait(15)


class UpbitAPINews(threading.Thread):
    def __init__(self, link):
        super(UpbitAPINews, self).__init__()
        self.link = link
        self.stop_event = threading.Event()
        self.old_list = {}

    def play(self, loop=True):
        while True:
            playsound(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'notification.wav')
            if not loop:
                break

    def stop(self):
        self.stop_event.set()

    def stopped(self):
        return self.stop_event.is_set()

    def display(self):
        if not self.old_list:
            print('Display not ready ... try again later' + "\n")
        else:
            print('Upbit News List : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            for list in self.old_list['list']:
                print(list)

    def diffrence(self, old, new):

        diff_list = Utils().str_diff(old, new)
        if diff_list:
            print('Upbit News List Detected : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            Utils().display_diff(diff_list)

    def run(self):
        new_list = {}
        while not self.stopped() and self.is_alive():
            try:
                page = requests.get(self.link)
                apiJSON = json.loads(page.content)
                if not self.old_list:
                    self.old_list['list'] = [item['title'] for item in apiJSON['data']['list']]
                    self.old_list['date'] = datetime.datetime.now()
                else:
                    new_list['list'] = [item['title'] for item in apiJSON['data']['list']]
                    self.old_list['date'], new_list['date'] = datetime.datetime.now(), datetime.datetime.now()
                    if self.old_list['list'] != new_list['list']:
                        try:
                            self.diffrence(self.old_list['list'], new_list['list'])
                        finally:
                            self.old_list['list'] = new_list['list']
                            self.play()

            except Exception as err:
                logger.error(err)
                logger.exception("message")
            self.stop_event.wait(15)

class bitFlyerNews(threading.Thread):
    def __init__(self, link):
        super(bitFlyerNews, self).__init__()
        self.link = link
        self.stop_event = threading.Event()
        self.old_list = {}

    def play(self, loop=True):
        while True:
            playsound(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'notification.wav')
            if not loop:
                break

    def stop(self):
        self.stop_event.set()

    def stopped(self):
        return self.stop_event.is_set()

    def display(self):
        if not self.old_list:
            print('Display not ready ... try again later' + "\n")
        else:
            print('bitFlyer News List : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            for list in self.old_list['list']:
                print(list)

    def diffrence(self, old, new):

        diff_list = Utils().str_diff(old, new)
        if diff_list:
            print('bitFlyer News List Detected : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            Utils().display_diff(diff_list)

    def run(self):
        new_list = {}
        while not self.stopped() and self.is_alive():
            try:
                page = requests.get(self.link)
                html = page.content
                parsed_html = BeautifulSoup(html, 'html.parser')

                if not self.old_list:
                    self.old_list['list'] = [item.img['alt'] for item in parsed_html.body.find_all('li', attrs={'class': 'item'})]
                    self.old_list['date'] = datetime.datetime.now()
                else:
                    new_list['list'] = [item.img['alt'] for item in parsed_html.body.find_all('li', attrs={'class': 'item'})]
                    self.old_list['date'], new_list['date'] = datetime.datetime.now(), datetime.datetime.now()
                    if self.old_list['list'] != new_list['list']:
                        try:
                            self.diffrence(self.old_list['list'], new_list['list'])
                        finally:
                            self.old_list['list'] = new_list['list']
                            self.play()

            except Exception as err:
                logger.error(err)
                logger.exception("message")

            self.stop_event.wait(15)


class bitFlyerAPINews(threading.Thread):
    def __init__(self, link):
        super(bitFlyerAPINews, self).__init__()
        self.link = link
        self.stop_event = threading.Event()
        self.old_list = {}

    def play(self, loop=True):
        while True:
            playsound(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'notification.wav')
            if not loop:
                break

    def stop(self):
        self.stop_event.set()

    def stopped(self):
        return self.stop_event.is_set()

    def display(self):
        if not self.old_list:
            print('Display not ready ... try again later' + "\n")
        else:
            print('bitFlyer API List : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            for list in self.old_list['list']:
                print(list)

    def diffrence(self, old, new):

        diff_list = Utils().str_diff(old, new)
        if diff_list:
            print('bitFlyer API List Detected : ' + self.old_list['date'].strftime("%Y-%m-%d %I:%M:%S") + "\n")
            Utils().display_diff(diff_list)

    def run(self):
        new_list = {}
        while not self.stopped() and self.is_alive():
            try:
                page = requests.post(self.link,data=json.dumps({"base_currency":"JPY","lang":"ja-JP"}),headers = {'content-type': 'application/json'})
                apiJSON = json.loads(page.content)
                if not self.old_list:
                    self.old_list['list'] = [item['currency_code'] for item in apiJSON['d']]
                    self.old_list['date'] = datetime.datetime.now()
                else:
                    new_list['list'] = [item['currency_code'] for item in apiJSON['d']]
                    self.old_list['date'], new_list['date'] = datetime.datetime.now(), datetime.datetime.now()
                    if self.old_list['list'] != new_list['list']:
                        try:
                            self.diffrence(self.old_list['list'], new_list['list'])
                        finally:
                            self.old_list['list'] = new_list['list']
                            self.play()

            except Exception as err:
                logger.error(err)
                logger.exception("message")
            self.stop_event.wait(15)

### FUNCTIONS ###

def display_title_bar():
    print("\t**********************************************")
    print("\t*** coin.Spider - Hello old and new coins! ***")
    print("\t**********************************************")



def get_user_choice():
    print("\n")
    print("[1] See a list of Intro Binance.")
    print("[2] See a list of News Binance.")
    print("[3] See a list of Intro OKex.")
    print("[4] See a list of News Okex.")
    print("[5] See a list of Tokens Bitfinex.")
    print("[6] See a list of Notice Huobi.")
    print("[7] See a list of News Huobi.")
    print("[8] See a list of News Upbit.")
    print("[9] See a list of News bitFlyer.")
    print("[10] See a list of Api bitFlyer.")
    print("[11] See a list of Api Binance.")

    print("[0] Start.")
    print("[q] Quit.")
    return input("What would you like to do? " + "\n" + "\n")


### MAIN PROGRAM ###

cmd = ''
Threads = []

display_title_bar()


BinanceIntroThread = BinanceIntro("https://support.binance.com/hc/en-us/sections/115000122291-Assets-Introduction")
Threads.append(BinanceIntroThread)

BinanceNewsThread = BinanceNews("https://support.binance.com/hc/en-us/sections/115000106672-New-Listings")
Threads.append(BinanceNewsThread)


OKexIntroThread = OKexIntro("https://support.okex.com/hc/en-us/sections/115000437971-Cryptocurrency-Intro")
Threads.append(OKexIntroThread)

OKexNewsThread = OKexNews("https://support.okex.com/hc/en-us/sections/115000447632-New-Token")
Threads.append(OKexNewsThread)


BitfinexTokensThread = BitfinexTokens("https://support.bitfinex.com/hc/en-us/sections/115001039645-Currencies-Tokens")
Threads.append(BitfinexTokensThread)


HuobiAPINoticeThread = HuobiAPINotice("https://www.huobi.com/p/api/contents/pro/list_notice?r=limit=10&language=en-us")
Threads.append(HuobiAPINoticeThread)

HuobiAPINewsThread = HuobiAPINews("https://www.huobi.com/p/api/contents/pro/single_page/?lang=en-us&pageType=1")
Threads.append(HuobiAPINewsThread)


UpbitAPINewsThread = UpbitAPINews("https://api-manager.upbit.com/api/v1/notices?page=1&per_page=20")
Threads.append(UpbitAPINewsThread)

bitFlyerNewsThread = bitFlyerNews("https://bitflyer.jp/en")
Threads.append(bitFlyerNewsThread)

bitFlyerAPINewsThread = bitFlyerAPINews("https://bitflyer.jp/ex.asmx/GetFxRate")
Threads.append(bitFlyerAPINewsThread)

BinanceAPIThread = BinanceAPI("https://www.binance.com/exchange/public/product")
Threads.append(BinanceAPIThread)


while cmd != 'q':
    cmd = get_user_choice()

    if cmd == '0':
        print("\n*** begin ...")
        [t.start() for t in Threads]
    elif cmd == '1':
        BinanceIntroThread.display()

    elif cmd == '2':
        BinanceNewsThread.display()

    elif cmd == '3':
        OKexIntroThread.display()

    elif cmd == '4':
        OKexNewsThread.display()

    elif cmd == '5':
        BitfinexTokensThread.display()

    elif cmd == '6':
        HuobiAPINoticeThread.display()

    elif cmd == '7':
        HuobiAPINewsThread.display()

    elif cmd == '8':
        UpbitAPINewsThread.display()

    elif cmd == '9':
        bitFlyerNewsThread.display()

    elif cmd == '10':
        bitFlyerAPINewsThread.display()

    elif cmd == '11':
        BinanceAPIThread.display()

    elif cmd == 'Q':
        [t.stop() for t in Threads]
        [t.join() for t in Threads]
        print("\nThanks for playing. Bye.")
        quit()

    else:
        print("\nI didn't understand that choice.\n")
