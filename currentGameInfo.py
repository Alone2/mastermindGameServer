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
        isGuesser = arguments["isGuesser"]

        ids_to_connect = mastermind.filestuff.getIdsToConnect(bool(isGuesser))
        return json.dumps(ids_to_connect)
    c = mastermind.connection().get(int(arguments["connection_id"]))
    info = {"isOver":c.isOver,"won":c.won,"ready":not c.isConnectable}
    return json.dumps(info)

if __name__ == "__main__":
    # Beim Starten wird die Funktion main ausgeführt
    main()