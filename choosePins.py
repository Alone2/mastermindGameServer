#!/usr/bin/env python
print("Content-type: text/html\n\n")
import cgi
import mastermind

def main():
    arguments = cgi.FieldStorage()
    if not ("connection_id" in arguments and "colors" in arguments and "tries" in arguments):
        return "error"

    mastermind.pins.save(int(arguments["connection_id"]), arguments["colors"], int(arguments["tries"]))

    return "received"

if __name__ == "__main__":
    # Beim Starten wird die Funktion main ausgeführt
    print(main())