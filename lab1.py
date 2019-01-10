#!/usr/bin/env python
import requests

print(requests.__version__)

#Python script to GET the Google homepage
r = requests.get("http://www.google.com")
print(r.status_code)
print(r.text)
#print(dir(r))

# raw URL to your Python script on GitHub
a = requests.get("https://raw.githubusercontent.com/chengze2/cmput404_lab1/master/lab1.py")
print(a.text)
