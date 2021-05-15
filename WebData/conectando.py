import socket
import re

url=input("Write the url:")
print(url)
host=re.findall("http://(.*)/",url)[0]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("{:}".format(host),80))
cmd = "GET {:} HTTP/1.0\r\n\r\n".format(url).encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()
