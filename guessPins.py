#!/usr/bin/env python
print("Content-type: text/html\n\n")
import cgi
import mastermind
import json

def main():
    arguments = cgi.FieldStorage()
    if not ("connection_id" in arguments and "colors" in arguments):
        return "error"

    guess = mastermind.pins.guess(int(arguments["connection_id"]), arguments["colors"])
    return json.dumps(guess)

if __name__ == "__main__":
    # Beim Starten wird die Funktion main ausgeführt
    main()