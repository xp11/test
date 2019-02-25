import socket
import time
import threading
import logging
logging.basicConfig(level=logging.INFO)


sock = socket.socket()
print(type(sock))
ip = '127.0.0.1'
port = 9999
ipaddr = (ip,port)
sock.bind(ipaddr)
sock.listen()
# time.sleep(100)
conn,_ = sock.accept()  #阻塞1
print(conn)
data = conn.recv(1024)  #阻塞2
print(data)
conn.send(data)

#
# class Tx:
#     def __init__(self,ip='127.0.0.1',port=9999):
#         self.ipaddr = (ip,port)
#         self.sock = socket.socket()
#         self.sock.bind(self.ipaddr)
#         self.clients = dict()
#
#     def start(self):
#         self.sock.listen()
#         threading.Thread(target=self.__accept,name='accept').start()
#
#     def stop(self):
#         pass
#
#
#
#     def __accept(self):
#         while True:
#             conn,ipinfo = self.sock.accept()
#             print(type(ipinfo))
#             logging.info(ipinfo)
#             self.clients[ipinfo] = conn
#             threading.Thread(target=self.__recv,args=(conn,ipinfo))
#
#     def __recv(self,conn:socket.socket,ipinfo):
#         while True:
#             data = conn.recv(1024)
#             data = data.decode()
#             if data == 'quit':
#                 self.clients.pop(ipinfo)
#                 break
#             mes = 'ack:{}'.format(data)
#             for client in self.clients.values():
#
#
# test=Tx()


