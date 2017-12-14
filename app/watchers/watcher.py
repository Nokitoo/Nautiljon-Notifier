class Watcher():
    sentItemsIds = []
    enabled = True

    def __init__(self, url, newItemsXPath, user):
        self.url = url
        self.newItemsXPath = newItemsXPath
        self.user = user

    def onNewItem(self, item):
        raise Exception('Should be overridden')
