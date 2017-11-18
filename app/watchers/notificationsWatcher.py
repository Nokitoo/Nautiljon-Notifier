from watchers import Watcher
from config import config
from utils import getResourceUrl, getUrlParam

class NotificationsWatcher(Watcher):
    def __init__(self):
        super().__init__('notificationsWatcher', config['notifications_url'], '//div[contains(@class, "toread")]')

    def onNewItem(self, item):
        # Note: don't forget the '.' at the beginning of the XPath to search from the notification node
        # The 'string' function allows to concatenate all the text nodes of the selected node
        title = item.xpath('string(.//*[contains(@class, "uneNoficiationTitre")]/text())')
        message = item.xpath('string(.//*[contains(@class, "uneNotificationMessage")])')
        iconUrl = getResourceUrl(item.xpath('string(.//*[contains(@class, "uneNotificationLien")]/img/@src)'))
        href = item.xpath('string(.//a[contains(@class, "uneNotificationLien")]/@href)')
        onClick = item.xpath('string(.//a[contains(@class, "uneNotificationLien")]/@onclick)')
        notificationId = getUrlParam(href, 'read');

        return {
            'itemId': notificationId,
            'title': title,
            'message': message,
            'iconUrl': iconUrl
        }
