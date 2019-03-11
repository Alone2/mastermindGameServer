#!/usr/bin/env python
print("Content-type: text/html\n\n")
import cgi
import mastermind
import json

def main():
    arguments = cgi.FieldStorage()
    if not "isGuesser" in arguments:
        return "error"
    if not "name" in arguments:
        if not  ("id_to_connect" in arguments):
            return "error"
        c = mastermind.connection()
        c_id2c = int(arguments["id_to_connect"].value)
        isGuesser = arguments["isGuesser"].value in ["True", "true", "1"]
        dat = c.newPlayer(c_id2c, isGuesser)
        c.save()
        data = {"id":dat, "info":arguments["info"].value}
        return json.dumps(data)
    
    c = mastermind.connection()
    name = arguments["name"].value
    isGuesser = arguments["isGuesser"].value in ["True", "true", "1"]
    c.new(name, isGuesser)
    c.save()

    data = {"id":c.id, "info":arguments["info"].value}
    return json.dumps(data)

if __name__ == "__main__":
    # Beim Starten wird die Funktion main ausgeführt
    print(main())