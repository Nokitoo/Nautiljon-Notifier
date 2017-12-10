class Watcher():
    def __init__(self, name, url, newItemsXPath, user):
        self.name = name
        self.url = url
        self.newItemsXPath = newItemsXPath
        self.user = user

        self.enabled = True

    def onNewItem(self, item):
        raise Exception('Should be overridden')
