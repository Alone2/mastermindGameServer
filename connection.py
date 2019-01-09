#!/usr/bin/env python
print("Content-type: text/html\n\n")
import cgi
import mastermind

def main():
    arguments = cgi.FieldStorage()
    if not ("name" in arguments and "isGuesser" in arguments):
        return "error"

    c = mastermind.connection().new(arguments["name"], bool(arguments["isGuesser"]))
    return c.id

if __name__ == "__main__":
    # Beim Starten wird die Funktion main ausgeführt
    main()