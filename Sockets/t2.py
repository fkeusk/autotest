import socket,threading,time
class Server():
    def __init__(self):
        host='localhost'
        port=555
        coninfo=(host,port)
        self.s=socket.socket()
        self.s.bind(coninfo)
        self.s.listen(10)
        self.users=[]
    def sends(self):
        while 1:
            con,addr=self.s.accept()
            self.users.append(con)
            t1=threading.Thread(target=self.sending,args=(con,addr,self.users))
            t1.start()
    def sending(self,con,addr,users):
        #
        con.send('Welcome,Please Enter You Name:'.encode('utf-8'))
        name=con.recv(1024).decode('utf-8')
        con.send('Set Name Success,Have a Chat!'.encode('utf-8'))
        while 1:
            x=con.recv(1024).decode('utf-8')
            info=time.strftime('%Y-%m-%d %X')+' '+name+'\n'+x
            print(info)
            for i in users:
                # y=i.recv(1024).decode('utf-8')
                i.send(info.encode('utf-8'))


s=Server()
s.sends()