#!/usr/bin/env python
print("Content-type: text/html\n\n")
import cgi
import mastermind

def main():
    arguments = cgi.FieldStorage()
    if not ("connection_id" in arguments and "colors" in arguments):
        return "error"

    #geht vlt. einfacher wenn connection.combination = colors
    mastermind.pins.save(int(arguments["connection_id"]), arguments["colors"])

    return "received"

if __name__ == "__main__":
    # Beim Starten wird die Funktion main ausgeführt
    main()