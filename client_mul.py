# encoding:utf-8
'''
Create on 2018-05-03
@author Zheng Huaiguo
2018-05-30 office
'''

import socket
import time
import struct

s=struct.Struct('!I4sf')

def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(message)
        print(message)
        response = s.unpack(bytes(sock.recv(1024)))
        print("接收:"+str(response))


HOST, PORT = "192.168.10.99", 8081
values=[1,b'hehe',100.56]
for i in range(10000):
    values[0]=i
    values[2]=i*1.2234
    print(values)
    packed_data=s.pack(*values)
    client(HOST, PORT, packed_data)
    time.sleep(0.6)
