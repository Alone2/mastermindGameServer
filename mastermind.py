import json
import random

class filestuff():
    @staticmethod
    def getIdsToConnect(isGuesser):
        data = filestuff.getJson(PATH)
        l = []
        for i,y in data.items():
            if y["isConnectable"] and y["hasGuesser"] != isGuesser:      
                l.append(y["id_to_connect"])
        return l
    @staticmethod
    def getIds():
        data = filestuff.getJson(PATH)
        ids = []
        for i in data:
            ids.append(i)
        return ids
    @staticmethod
    def getId(id_to_connect):
        data = filestuff.getJson(PATH)
        for i,y in data.items():
            if y["id_to_connect"] == id_to_connect:
                return i
        return None
    @staticmethod
    def saveJson(path, data):
        dataJSON = json.dumps(data, indent=2)
        jsonFile = open(path, 'w')
        jsonFile.write(dataJSON)
        jsonFile.close()
    @staticmethod
    def getJson(path):
        jsonFile = open(path, 'r')
        data = json.loads(jsonFile.read())
        jsonFile.close()
        return data

class pins():
    @staticmethod
    def save(connection_id, colors, tries):
        c = connection()
        c.get(connection_id)
        c.tries = tries
        c.combination = colors
        c.isConnectable = False
        c.save()
    @staticmethod
    def guess(connection_id, my_colors):
        c = connection()
        c.get(connection_id)
        c.user_combinations.append(my_colors)
        c.user_tries += 1
        
        correct = 0
        correctC = 0

        # TO-DO: TEST IF CORRECT

        cor = {"correct":correct, "correctColor":correctC}
        c.correct_combinations.append(cor)

        if correct >= len(my_colors):
            #Chooser lost
            c.won = False
            c.isOver = True
        elif c.user_tries >= c.tries:
            # Chooser won
            c.won = True
            c.isOver = True  
        c.save()
        return cor

class connection():
    def __init__(self):
        self.id = 0
        self.isConnectable = True
        self.hasGuesser = None
        self.name = ""
        self.id_to_connect = 0
        self.isOver = False
        self.won = None
        self.tries = 10
        self.user_tries = 0
        self.combination = []
        self.user_combinations = []
        self.correct_combinations = []
    
    def new(self, name, isGuesser):
        self.name = name
        self.id = self.__generateId(10, filestuff.getIds())
        self.id_to_connect = self.__generateId(10, filestuff.getIdsToConnect(isGuesser))
        self.hasGuesser = isGuesser
        
    def get(self, my_id):
        data = filestuff.getJson(PATH)
        data_myid = data[str(my_id)]
        self.id = my_id
        self.isConnectable = data_myid["isConnectable"]
        self.hasGuesser = data_myid["hasGuesser"]
        self.name = data_myid["name"]
        self.id_to_connect = data_myid["id_to_connect"]
        self.isOver = data_myid["isOver"]
        self.won = data_myid["won"]
        self.tries = data_myid["tries"]
        self.user_tries = data_myid["user_tries"]
        self.combination = data_myid["combination"]
        self.user_combinations = data_myid["user_combinations"]
        self.correct_combinations = data_myid["correct_combinations"]
    
    def newPlayer(self, id_to_connect, isGuesser):
        new_id = filestuff.getId(id_to_connect)
        if new_id == 0:
            return "error"
        self.get(new_id)
        if self.isConnectable == False:
            return "error"
        if self.hasGuesser == isGuesser:
            return "error"
        self.isConnectable = False
        return self.id

    def save(self):
        data = filestuff.getJson(PATH)
        data[str(self.id)] = {
            "isConnectable":self.isConnectable,
            "hasGuesser":self.hasGuesser,
            "name":self.name,
            "id_to_connect":self.id_to_connect,
            "isOver":self.isOver,
            "won":self.won,
            "tries":self.tries,
            "combination":self.combination,
            "user_combinations":self.user_combinations,
            "user_tries":self.user_tries,
            "correct_combinations":self.correct_combinations
        }
        filestuff.saveJson(PATH, data)

    def delete(self):
        data = filestuff.getJson(PATH)
        del data[str(self.id)]
        filestuff.saveJson(PATH, data)

    def __generateId(self, lenght, notValidIds = []):
        new_id = ""
        for i in range(lenght):
            new_id += random.choice("1234567890")

        if new_id in notValidIds:
            new_id = self.__generateId(lenght, notValidIds)

        return int(new_id)

PATH = filestuff.getJson("config.json")["data_path"]
