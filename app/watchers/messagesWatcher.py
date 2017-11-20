from watchers import Watcher
from config import config
from utils import getResourceUrl, getUrlParam

class MessagesWatcher(Watcher):
    def __init__(self, user):
        super().__init__('messages_watcher', config['messages_url'], '//table[@id="list_messages"]//tr[td//img[@alt="Nouveau message"]]', user)

    def onNewItem(self, item):
        sender = item.xpath('string(.//div[contains(@class, "cropMembre")])')
        subject = item.xpath('string(.//a[contains(@href, "/messagerie")]/text())')
        url = item.xpath('string(.//a[contains(@href, "/messagerie")]/@href)')
        messageId = getUrlParam(url, 'lire');

        return {
            'itemId': messageId,
            'url': getResourceUrl(url),
            'title': 'Nouveau message',
            'message': '{0}\nDe {1}'.format(subject, sender),
            'iconUrl': 'nautiljon_icon.ico'
        }
