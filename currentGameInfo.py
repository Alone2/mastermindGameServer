#!/usr/bin/env python
print("Content-type: text/html\n\n")
import cgi
import mastermind
import json

def main():
    arguments = cgi.FieldStorage()
    if not "connection_id" in arguments:
        if not "isGuesser" in arguments:
            return "error"
        isGuesser = arguments["isGuesser"].value in ["True", "true", "1"]

        ids_to_connect = mastermind.filestuff.getIdsToConnect(isGuesser)
        id_and_name = []
        for i in ids_to_connect:
            c = mastermind.connection()
            if not c.get(i):
                id_and_name.append({"id":i,"name":"error"})
                continue
            id_and_name.append({"id":i,"name":c.name})   
        finalData = {"ids": id_and_name, "info":arguments["info"].value}
        return json.dumps(finalData)

    c = mastermind.connection()
    c_id = int(arguments["connection_id"].value)
    if not c.get(c_id):
        return "error"
    info = {"info":arguments["info"].value,"isGuessable":c.isGuessable,"isOver":c.isOver,"won":c.won,"ready": not c.isConnectable, "user_combinations":c.user_combinations, "correct_combinations":c.correct_combinations, "numTries":c.tries, "numColors":c.numColors}

    if c.isOver:
        c.delete()
    return json.dumps(info)

if __name__ == "__main__":
    # Beim Starten wird die Funktion main ausgeführt
    print(main())
