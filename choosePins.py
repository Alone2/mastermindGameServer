#!/usr/bin/env python
print("Content-type: text/html\n\n")
import cgi
import mastermind

def main():
    arguments = cgi.FieldStorage()
    if not ("connection_id" in arguments and "colors" in arguments and "tries" in arguments):
        return "error"

    c_id = int(arguments["connection_id"].value)
    colors = arguments["colors"].value
    tries = int(arguments["tries"].value)

    mastermind.pins.save(c_id, colors, tries)

    return "received"

if __name__ == "__main__":
    # Beim Starten wird die Funktion main ausgeführt
    print(main())