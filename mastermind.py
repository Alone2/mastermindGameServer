import json

class filestuff():
    @staticmethod
    def getIdsToConnect(isGuesser):
        return []
    @staticmethod
    def getIds():
        return []
    @staticmethod
    def getId(id_to_connect):
        return 0
    @staticmethod
    def saveJson(file, data):
        pass
    @staticmethod
    def getJson(file):
        pass

class pins():
    @staticmethod
    def save(connection_id, colors):
        pass
    @staticmethod
    def guess(connection_id, my_colors):
        pass


class connection():
    def __init__(self):
        self.id = 0
        self.isConnectable = True
        self.hasGuesser = None
        self.name = ""
        self.id_to_connect = 0
        self.isOver = False
        self.won = ""
        self.tries = 10
    
    def new(self, name, isGuesser):
        self.name = name
        self.id = self.__generateId(filestuff.getIds())
        self.id_to_connect = self.__generateId(filestuff.getIdsToConnect(isGuesser))
        
    def get(self, id):
        pass
    
    def newPlayer(self, id_to_connect, isGuesser):
        new_id = filestuff.getId(id_to_connect)
        if new_id == 0:
            return "error"
        self.get(new_id)
        if self.isConnectable == False:
            return "error"
        self.isConnectable = False
    
    def __generateId(self, notValidIds = []):
        return 0

    