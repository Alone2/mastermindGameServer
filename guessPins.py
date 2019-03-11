#!/usr/bin/env python
print("Content-type: text/html\n\n")
import cgi
import mastermind
import json

def main():
    arguments = cgi.FieldStorage()
    if not ("connection_id" in arguments and "colors" in arguments):
        return "error"
    
    c_id = int(arguments["connection_id"].value)
    colors = arguments["colors"].value
    guess = mastermind.pins.guess(c_id, colors)

    guess["info"] =  arguments["info"].value
    return json.dumps(guess)

if __name__ == "__main__":
    # Beim Starten wird die Funktion main ausgeführt
    print(main())