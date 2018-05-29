# coding:utf-8
'''
Create on 2018-05-03
@author Zheng Huaiguo
2018-05-029 bakcup to git
'''

import socketserver
import struct
import redis

r = redis.Redis(host='127.0.0.1', port=6379,db=0)
s=struct.Struct('!I4sf')
list=[]
#继承StreamRequestHandler类，并重写其中的handle方法，该方法是在每个请求到来之后都会调用
class ThreadedTCPRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        #这里是将传进的数据加上Hello 之后再返回，继承自StreamRequestHandler可以使用wfile这个类文件（file-like）对象
        data = bytes(self.request.recv(1024))
        unpackdata=s.unpack(data)
        print(unpackdata)
        r.set('id',unpackdata[0])
        r.set('strgood',unpackdata[1])
        r.set('numf',unpackdata[2])
        data =s.pack(*unpackdata)
        self.wfile.write(data) #write()方法只能写入bytes类型

#该类是实现多请求并发处理，只需要继承socketserver.ThreadingMixIn即可，内部无需多加处理，采用默认方法。
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    #如果是在局域网内实现通信，则必须将地址绑定在该PC在局域网中的地址
    #如果只是本机通信则为"localhost"或者"127.0.0.1"即可
    HOST, PORT = "192.168.10.99",8081
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    server.serve_forever()
    print('bye')
        
