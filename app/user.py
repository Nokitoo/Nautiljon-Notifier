import requests
import logging
from lxml import etree
from lxml.etree import fromstring
import time

from PyQt5.QtCore import QObject, pyqtSignal

class User(QObject):
    finished = pyqtSignal(bool)
    username = ""

    def __init__(self):
        super().__init__()
        logging.debug('qsdqdsqsd')
        self.session = None
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'})
        r = self.session.get('https://www.nautiljon.com/')
        logging.debug('Cookies : %s', r.cookies.get_dict())

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
            r = self.session.post('https://www.nautiljon.com/membre/login.php', data=data)

            # Debug
            logging.debug(r.text)
            logging.debug('Status Code : %s', r.status_code)
            logging.debug('Cookies : %s', r.cookies.get_dict())

            # Search for error div
            # (If there is an error, a 200 response is sent)
            tree = etree.HTML(r.text.encode('utf-8'))
            error = tree.xpath('//div[@id="inscription"]//div[@id="errors"]')
            if len(error) == 0:
                self.username = username
                self.finished.emit(True)
            else:
                self.finished.emit(False)

        except Exception as err:
            logging.debug('Exception thrown')
            logging.debug(err)
            self.finished.emit(False)
