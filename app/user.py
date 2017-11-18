import os
import requests
import logging
from lxml import etree
import time
import json

from PyQt5.QtCore import QObject, pyqtSignal, QUrl, QThread
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtGui import QIcon, QImage, QPixmap

from config import config
from decorators import autoCreateDir
from watcherManager import WatcherManager
import urllib.parse as urlparse


@autoCreateDir(config['data_dir_path'])
class User(QObject):
    finished = pyqtSignal(bool)
    startWatchNotifications = pyqtSignal(QObject)
    retrievedAvatarSignal = pyqtSignal(requests.Response)

    username = ""
    avatar = None
    connected = False
    userSaveFilePath = os.path.join(config['data_dir_path'], 'user.json')

    def __init__(self):
        super().__init__()
        self.retrievedAvatarSignal.connect(self.retrieveAvatarFromReq)

    # Don't init in construtor because we need logs
    def init(self, displayNotification):
        # Init watcher manager and watchers with time interval of 1 minute
        self.watcherManager = WatcherManager(1)
        self.watcherManager.onNewNotification.connect(displayNotification)
        self.initWatchers()

        # Setup thread for watcher manager
        # TODO: Add mutex for resources access
        self.workerThread = QThread()
        self.watcherManager.moveToThread(self.workerThread)
        self.workerThread.start()
        # We need to use a signal to call watcherManager.watchNotification or it won't be in thead context
        self.startWatchNotifications.connect(self.watcherManager.startWatchNotifications)

        # Load user cookies from file
        cookies = None
        if os.path.exists(self.userSaveFilePath):
            logging.debug('Loading cookies')
            try:
                with open(self.userSaveFilePath, 'r+') as f:
                    cookiesStr = f.read()
                    logging.debug('Cookies : %s', cookiesStr)
                    cookies = requests.utils.cookiejar_from_dict(json.loads(cookiesStr))
            except IOError as err:
                logging.error('Failed to load cookies %s', str(err))

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
            logging.debug('User is connected')
            self.retrievedAvatarSignal.emit(req)
            self.connected = True
            self.startWatchNotifications.emit(self)


    def initWatchers(self):

        def getUrlParam(url, param):
            parsed = urlparse.urlparse(url)
            return urlparse.parse_qs(parsed.query)[param]

        def getResourceUrl(url):
            # '/resource.png' => 'http://www.site/resource.png'
            if url and url[0] == '/':
                return config['site_domain'] + url;

            return url;

        def onNewNotification(item):
            # Note: don't forget the '.' at the beginning of the XPath to search from the notification node
            # The 'string' function allows to concatenate all the text nodes of the selected node
            title = item.xpath('string(.//*[contains(@class, "uneNoficiationTitre")]/text())')
            message = item.xpath('string(.//*[contains(@class, "uneNotificationMessage")])')
            iconUrl = getResourceUrl(item.xpath('string(.//*[contains(@class, "uneNotificationLien")]/img/@src)'))
            href = item.xpath('string(.//a[contains(@class, "uneNotificationLien")]/@href)')
            onClick = item.xpath('string(.//a[contains(@class, "uneNotificationLien")]/@onclick)')
            notificationId = getUrlParam(href, 'read');

            logging.debug('New notification')

            return {
                'itemId': notificationId,
                'title': title,
                'message': message,
                'iconUrl': iconUrl
            }

        notificationsWatcher = {}
        notificationsWatcher['name'] = 'notificationsWatcher'
        notificationsWatcher['url'] = config['notifications_url']
        notificationsWatcher['newItemsXPath'] = '//div[contains(@class, "toread")]'
        notificationsWatcher['onNewItem'] = onNewNotification

        self.watcherManager.addWatcher(notificationsWatcher)

    def initSession(self, cookies = None):
        # Init session
        self.session = None
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'})

        if cookies:
            self.session.cookies = cookies

        # Make a first call to have session cookies
        # (/membre/login.php won't give us a session cookie)
        req = self.session.get(config['home_url'])

        return req if req.status_code == 200 else None

    # Save cookies to file
    def cleanUp(self):
        logging.debug('Saving cookies')
        with open(self.userSaveFilePath, 'w+') as f:
            cookies = requests.utils.dict_from_cookiejar(self.session.cookies)
            cookiesStr = json.dumps(cookies)
            logging.debug('Cookies : %s', cookiesStr)
            f.write(cookiesStr)

        self.watcherManager.stopWatchNotifications()
        if self.watcherManager.isWaiting:
            self.workerThread.terminate()
        self.workerThread.quit()
        self.workerThread.wait()

    def retrieveAvatarFromReq(self, req):
        logging.debug('Retrieve user avatar')

        def imageRetrieved(reply):
            logging.debug('Avatar retrieved')
            img = QImage()
            img.loadFromData(reply.readAll())
            self.avatar = QIcon(QPixmap(img).scaled(32, 32))

        tree = etree.HTML(req.text.encode('utf-8'))
        avatarPath = tree.xpath('string(//div[@id="espace_membre"]//img/@src)')
        if avatarPath:
            url = config['site_domain'] + avatarPath
            logging.debug('Avatar url : %s', url)
            self.accessManager = QNetworkAccessManager()
            self.accessManager.finished.connect(imageRetrieved)
            self.accessManager.get(QNetworkRequest(QUrl(url)))


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
                'r': config['login_url']
            }
            req = self.session.post(config['login_url'], data=data)

            # Debug
            logging.debug('Status Code : %s', req.status_code)
            logging.debug('Cookies : %s', req.cookies.get_dict())

            # Search for connection error div
            tree = etree.HTML(req.text.encode('utf-8'))
            error = tree.xpath('//div[@id="inscription"]//div[@id="errors"]')
            if len(error) == 0:
                self.username = username
                self.connected = True
                self.finished.emit(True)
                self.retrievedAvatarSignal.emit(req)
                self.startWatchNotifications.emit(self)
            else:
                self.finished.emit(False)

        except Exception as e:
            logging.error('Failed to connect : %s', e)
            self.finished.emit(False)
