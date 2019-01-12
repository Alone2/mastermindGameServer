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
        c_id2c = int(arguments["id_to_connect"].value)
        isGuesser = arguments["isGuesser"].value in ["True", "true", "1"]
        return c.newPlayer(c_id2c, isGuesser)
    
    c = mastermind.connection()
    name = arguments["name"].value
    isGuesser = arguments["isGuesser"].value in ["True", "true", "1"]
    c.new(name, isGuesser)
    c.save()

    return c.id

if __name__ == "__main__":
    # Beim Starten wird die Funktion main ausgeführt
    print(main())