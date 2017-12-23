import os
import requests
import logging
from lxml import etree
import json

from PyQt5.QtCore import QObject, pyqtSignal, QThread

from config import config
from decorators import autoCreateDir
from watcherManager import WatcherManager
from watchers import NotificationsWatcher, MessagesWatcher
from userSettings import UserSettings


@autoCreateDir(config['data_dir_path'])
class User(QObject):
    onFinishedConnect = pyqtSignal(str, bool)
    startWatchNotifications = pyqtSignal(QObject)

    avatar = None
    connected = False
    userSaveFilePath = os.path.join(config['data_dir_path'], 'user.json')

    def __init__(self):
        super().__init__()
        self.settings = UserSettings()

    # Don't init in construtor because we need logs
    def init(self, mainWindow):
        # Load user session and settings from file
        cookies = None
        if os.path.exists(self.userSaveFilePath):
            logging.debug('Reading user file')
            try:
                with open(self.userSaveFilePath, 'r+') as f:
                    userDataStr = f.read()
                    logging.debug('User data : %s', userDataStr)
                    userDataJson = json.loads(userDataStr)

                    # Load settings
                    self.settings.loadFromJson(userDataJson)

                    # Retrieve sessid cookies
                    cookies = requests.utils.cookiejar_from_dict(userDataJson['sessid'])
            except Exception as e:
                logging.exception('Failed to load cookies')

        self.initWatchers(mainWindow)

        req = self.initSession(cookies)
        # Fail to get page (Invalid session ?)
        if not req:
            # Retry with fresh cookies
            req = self.initSession()
            # Fail with fresh cookies
            if not req:
                self.onFinishedConnect.emit(None, False)
                return;

        if self.reqContainsRegisterButton(req):
            logging.debug('User is connected')
            self.connected = True
            self.onFinishedConnect.emit(None, True)
            self.startWatchNotifications.emit(self)
        else:
            self.onFinishedConnect.emit(None, False)

    def reqContainsRegisterButton(self, req):
        if not req:
            return False

        tree = etree.HTML(req.text.encode('utf-8'))
        registerButton = tree.xpath('//a[@id="btn_insc"]')

        return len(registerButton) == 0

    def initWatchers(self, mainWindow):
        # Init watcher manager and watchers with time interval of 1 minute
        self.watcherManager = WatcherManager(1)
        self.watcherManager.onNewNotification.connect(mainWindow.onNewNotification)
        self.watcherManager.onUserDisconnected.connect(mainWindow.onUserDisconnected)

        # Setup thread for watcher manager
        # TODO: Add mutex for resources access
        self.workerThread = QThread()
        self.watcherManager.moveToThread(self.workerThread)
        self.workerThread.start()
        # We need to use a signal to call watcherManager.watchNotification or it won't be in thread context
        self.startWatchNotifications.connect(self.watcherManager.startWatchNotifications)

        # Init watchers
        self.notificationsWatcher = NotificationsWatcher(self)
        self.messagesWatcher = MessagesWatcher(self)
        self.watcherManager.addWatcher(self.notificationsWatcher)
        self.watcherManager.addWatcher(self.messagesWatcher)

        self.updateWatchers()

    def updateWatchers(self):
        self.notificationsWatcher.enabled = self.settings.notifications;
        self.messagesWatcher.enabled = self.settings.messages;

    def initSession(self, cookies = None):
        # Init session
        self.session = None
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'})

        if cookies:
            self.session.cookies = cookies

        # Make a first call to have session cookies
        # (/membre/login.php won't give us a session cookie)
        try:
            req = self.session.get(config['home_url'])
        except Exception as e:
            logging.exception('Failed to init session')
            return None

        return req if req.status_code == 200 else None

    def cleanUp(self):
        self.saveData()

        self.watcherManager.stopWatchNotifications()

        # Wait only if worker is doing job
        # Otherwise, force exit
        if not self.watcherManager.isWaiting:
            self.workerThread.quit()
            self.workerThread.wait()

    # Save cookies and settings to file
    def saveData(self):
        logging.debug('Saving user data')
        with open(self.userSaveFilePath, 'w+') as f:
            userData = {}
            userData['sessid'] = requests.utils.dict_from_cookiejar(self.session.cookies)
            userData['settings'] = {}
            userData['settings']['notifications'] = self.settings.notifications
            userData['settings']['messages'] = self.settings.messages
            userData['settings']['notifications_close_seconds'] = self.settings.notificationsCloseSeconds

            logging.debug('User data : %s', userData)

            f.write(json.dumps(userData))

    def connect(self, username, password):
        logging.debug('Connecting user...')

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
                self.connected = True
                self.onFinishedConnect.emit(None, True)
                self.startWatchNotifications.emit(self)
            else:
                self.onFinishedConnect.emit("Mauvais identifiants", False)

        except Exception as e:
            logging.exception('Failed to connect')
            self.onFinishedConnect.emit("Erreur de connexion", False)
