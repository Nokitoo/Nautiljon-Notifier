import os
import requests
import logging
from lxml import etree
from lxml.etree import fromstring
import time
import json

from PyQt5.QtCore import QObject, pyqtSignal

class User(QObject):
    finished = pyqtSignal(bool)
    username = ""
    connected = False
    userSaveFilePath = os.path.join(os.path.dirname(__file__), 'user.json')

    def __init__(self):
        super().__init__()

        # Load user cookies from file
        cookies = None
        if os.path.exists(self.userSaveFilePath):
            logging.debug('Loading cookies')
            with open(self.userSaveFilePath, 'r+') as f:
                cookies = requests.utils.cookiejar_from_dict(json.loads(f.read()))


        req = self.initSession(cookies)
        # Fail to get page (Invalid session ?)
        if not req:
            # Retry with fresh cookies
            req = self.initSession()
            # Fail with fresh cookies
            if not req:
                return;

        # Search for register button to know if the user is connected
        tree = etree.HTML(req.text.encode('utf-8'))
        registerButton = tree.xpath('//a[@id="btn_insc"]')
        if len(registerButton) == 0:
            self.connected = True


    def initSession(self, cookies = None):
        # Init session
        self.session = None
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'})

        if cookies:
            self.session.cookies = cookies

        # Make a first call to have session cookies
        # (/membre/login.php won't give us a session cookie)
        req = self.session.get('https://www.nautiljon.com/')

        return req if req.status_code == 200 else None

    # Save cookies to file
    def cleanUp(self):
        logging.debug('Saving cookies')
        with open(self.userSaveFilePath, 'w+') as f:
            cookies = requests.utils.dict_from_cookiejar(self.session.cookies)
            cookiesStr = json.dumps(cookies)
            logging.debug('Cookies : %s', cookiesStr)
            f.write(cookiesStr)


    def connect(self, username, password):
        logging.debug('Connecting user...')
        logging.debug('Username : %s', username)
        logging.debug('Password : %s', password)

        # Try to connect
        try:
            # Send request
            data = {
                'login': username,
                'pass': password,
                'lcookie': 'on',
                'r': 'https://www.nautiljon.com/membre/login.php'
            }
            req = self.session.post('https://www.nautiljon.com/membre/login.php', data=data)

            # Debug
            logging.debug(req.text)
            logging.debug('Status Code : %s', req.status_code)
            logging.debug('Cookies : %s', req.cookies.get_dict())

            # Search for error div
            # (If there is an error, a 200 response is sent)
            tree = etree.HTML(req.text.encode('utf-8'))
            error = tree.xpath('//div[@id="inscription"]//div[@id="errors"]')
            if len(error) == 0:
                self.username = username
                self.connected = True
                self.finished.emit(True)
            else:
                self.finished.emit(False)

        except Exception as err:
            logging.debug('Exception thrown')
            logging.debug(err)
            self.finished.emit(False)
