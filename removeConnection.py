#!/usr/bin/env python
print("Content-type: text/html\n\n")
import cgi
import mastermind
import json

def main():
    arguments = cgi.FieldStorage()
    if not "connection_id" in arguments:
        return "error"

    c = mastermind.connection()
    c_id = int(arguments["connection_id"].value)
    if not c.get(c_id):
        return "error"
    
    output = ""
    if c.isConnectable:
        c.delete()
        output = "done"
    else:
        output = "error"

    info = {"info":arguments["info"].value, "action":output}
    return json.dumps(info)

if __name__ == "__main__":
    # Beim Starten wird die Funktion main ausgeführt
    print(main())