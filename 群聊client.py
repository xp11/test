from socket import socket,SOCK_DGRAM
import threading

class SocketClient:
    def __init__(self,ip='192.168.0.3',port=9999):
        self.ip = ip
        self.port = port
        self.sock =socket(type=SOCK_DGRAM)



    def start(self):
        self.send('reg')
        threading.Thread(target=self.recv).start()


    def stop(self):
        self.sock.close()

    def recv(self):
        while True:
            data = self.sock.recv(1024)
            print(data)
    def send(self,mes):
        data = mes.encode()
        self.sock.sendto(data,(self.ip,self.port))





if __name__ == '__main__':
    client = SocketClient()
    client.start()
    while True:
        mes = input(">>>")
        if mes == 'quit':
            client.stop()
            break
        client.send()