class Watcher():
    def __init__(self, name, url, newItemsXPath):
        self.name = name
        self.url = url
        self.newItemsXPath = newItemsXPath

    def onNewItem(self, item):
        raise Exception('Should be overridden')
