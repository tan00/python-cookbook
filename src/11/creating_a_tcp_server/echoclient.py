from socket import socket, AF_INET, SOCK_STREAM
from time import sleep

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))

s.send(b'Hello00000Hello00000Hello00000Hello00000\n')

sleep(1)
resp = s.recv(8192)

s.close()
print('Response:', resp)



