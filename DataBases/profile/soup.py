import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter  ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
#for line in html:
#print(line.decode().strip())

#Retrieve all of the all the anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get("href",None))
