import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')

fhand=urllib.request.urlopen(url)
data=fhand.read()

tree =ET.fromstring(data)
counts = tree.findall('.//count')
numbers=list()
for count in counts:
    numbers.append(int(count.text))
print(sum(numbers))
    
