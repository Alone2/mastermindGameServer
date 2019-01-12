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
        return json.dumps(ids_to_connect)

    c = mastermind.connection()
    c_id = int(arguments["connection_id"].value)
    c.get(c_id)
    info = {"isOver":c.isOver,"won":c.won,"ready": not c.isConnectable, "user_combinations":c.user_combinations}

    if c.isOver:
        c.delete()
    return json.dumps(info)

if __name__ == "__main__":
    # Beim Starten wird die Funktion main ausgeführt
    print(main())