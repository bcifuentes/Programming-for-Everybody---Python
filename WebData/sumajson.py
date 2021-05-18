import urllib.request , urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input("Enter url:")

data= urllib.request.urlopen(url).read().decode()

js=json.loads(data)
numbers=[]
for comment in js["comments"]:
    numbers.append(int(comment["count"]))

print(sum(numbers))
