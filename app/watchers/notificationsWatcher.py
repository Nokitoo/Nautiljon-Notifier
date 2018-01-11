import logging
import re

from watchers import Watcher
from config import config
from utils import getResourceUrl, getUrlParam

class NotificationsWatcher(Watcher):
    def __init__(self, user):
        super().__init__(config['notifications_url'], '//div[contains(@class, "toread")]', user)

    def onNewItem(self, item):
        # Note: don't forget the '.' at the beginning of the XPath to search from the notification node
        # The 'string' function allows to concatenate all the text nodes of the selected node
        title = item.xpath('string(.//*[contains(@class, "uneNoficiationTitre")]/text())')
        message = item.xpath('string(.//*[contains(@class, "uneNotificationMessage")])')
        iconUrl = getResourceUrl(item.xpath('string(.//*[contains(@class, "uneNotificationLien")]/img/@src)'))
        href = item.xpath('string(.//a[contains(@class, "uneNotificationLien")]/@href)')
        notificationId = getUrlParam(href, 'read');

        return {
            'itemId': notificationId,
            'url': getResourceUrl(href),
            'title': title,
            'message': message,
            'iconUrl': iconUrl
        }
