import logging
import re

from watchers import Watcher
from config import config
from utils import getResourceUrl, getUrlParam

class NotificationsWatcher(Watcher):
    def __init__(self, user):
        super().__init__('notificationsWatcher', config['notifications_url'], '//div[contains(@class, "toread")]', user)

    def onNewItem(self, item):
        # Note: don't forget the '.' at the beginning of the XPath to search from the notification node
        # The 'string' function allows to concatenate all the text nodes of the selected node
        title = item.xpath('string(.//*[contains(@class, "uneNoficiationTitre")]/text())')
        message = item.xpath('string(.//*[contains(@class, "uneNotificationMessage")])')
        iconUrl = getResourceUrl(item.xpath('string(.//*[contains(@class, "uneNotificationLien")]/img/@src)'))
        href = item.xpath('string(.//a[contains(@class, "uneNotificationLien")]/@href)')
        onClick = item.xpath('string(.//a[contains(@class, "uneNotificationLien")]/@onclick)')
        notificationId = getUrlParam(href, 'read');

        url = re.findall(r"'[^']+'", str(onClick))[-1]

        def onClickHandler():
            try:
                self.user.session.get(getResourceUrl(href))
            except Exception as e:
                logging.exception('Cannot read notification %s', notificationId)

        return {
            'itemId': notificationId,
            'url': getResourceUrl(url.replace('\'', '')),
            'title': title,
            'message': message,
            'iconUrl': iconUrl,
            'onClick': onClickHandler
        }
