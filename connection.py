#!/usr/bin/env python
print("Content-type: text/html\n\n")
import cgi
import mastermind

def main():
    arguments = cgi.FieldStorage()
    if not "isGuesser" in arguments:
        return "error"
    if not "name" in arguments:
        if not  ("id_to_connect" in arguments):
            return "error"
        c = mastermind.connection()
        return c.newPlayer(int(arguments["id_to_connect"]), bool(arguments["isGuesser"]))
    
    c = mastermind.connection()
    c.new(arguments["name"], bool(arguments["isGuesser"]))
    return c.id

if __name__ == "__main__":
    # Beim Starten wird die Funktion main ausgeführt
    print(main())