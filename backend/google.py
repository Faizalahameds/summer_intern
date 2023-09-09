#!/usr/bin/python3

import subprocess as s
import cgi
from googlesearch import search


print("Content-Type:text/html")
print()

form = cgi.FieldStorage()
data=form.getvalue("search")


def google_search(query):
    top_results = list(search(query, num_results=5))
    print("<pre><h1>")
    print(f"\nTop 5 results for '{query}':\n")
    print("</h1>")
    for idx, result in enumerate(top_results, start=1):
        print("<h2>")
        print(f"{idx}. {result}")
        print("</h2>")
        print("<br>")
    print("</pre>")
try:
 google_search(data)

except:
    print("<h2>Error connecting to internet</h2>")