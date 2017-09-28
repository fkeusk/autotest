import socket
class Client():
    def __init__(self):
        host='localhost'
        port=555
        coninfo=(host,port)
        self.c=socket.socket()
        self.c.connect(coninfo)

    def sendname(self):
        x=self.c.recv(1024).decode('utf-8')
        print(x)
        self.c.send(input().encode('utf-8'))
        y=self.c.recv(1024).decode('utf-8')
        print(y)
        # while 1:
    def sends(self):
        while 1:
            z=input('请发送消息：').encode('utf-8')
            self.c.send(z)

    def receive(self):
        while 1:
            x=self.c.recv(1024).decode('utf-8')
            if x!='':
                print(x)

c=Client()
c.sendname()
c.sends()
