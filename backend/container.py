#!/usr/bin/python3
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print("Content-type: text/html")
print()

import subprocess

command = "sudo docker ps -a"

exitcode, output = subprocess.getstatusoutput(command)

if exitcode == 0:
    totalcontainer = output.split('\n')[1:]
    table_content = "<table width='100%' align='center' border=5>"
    table_content += """<tr bgcolor='green'><th>ID</th><th>Image</th><th>Status</th><th>Name</th></tr>"""
    for container in totalcontainer:
        table_content += "<tr>"
        table_content += "<td>" + container.split()[0] + "</td>"
        table_content += "<td>" + container.split()[1] + "</td>"
        table_content += "<td>" + container.split()[6] + "</td>"
        table_content += "<td>" + container.split()[-1] + "</td>"
        table_content += "</tr>"
    table_content += "</table>"
else:
    table_content = "<p>Retry</p>"

# Display HTML template with table content
with open("/var/www/html/dockercontainer.html", "r") as html_file:
    html_content = html_file.read()
     print(html_content.replace("{{table_content}}", table_content))