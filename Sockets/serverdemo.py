import socket,time,threading,sys
class service():
    users=[]
    def __init__(self):
        self.s = socket.socket()
        host='localhost'
        port=555
        coninfo = (host,port)
        self.s.bind(coninfo)
        self.s.listen(5)

    def connections(self):
        while 1:
            namedict={}
            con, addr=self.s.accept()
            con.send('connect successfully...!\tenter a name please'.encode('utf-8'))
            self.users.append(con)
            threading.Thread(target=self.send_info,args=((con,addr,namedict))).start()
            # (con.recv(1024).decode('utf-8'))=addr[0]
    def send_info(self,con,addr,namedict):
        x=con.recv(1024).decode('utf-8')
        namedict.update({addr:x})
        con.send('Set successfully!'.encode('utf-8'))
        while 1:
            data=con.recv(1024).decode('utf-8')
            info=x+' '+time.strftime('%Y-%m-%d %X')+':'+'\n'+data
            print(info)
            for i in self.users:
                i.send(info.encode('utf-8'))
            if data=='quit':
                self.s.close()
                sys.exit()
            # con.send(input('answer:').encode('utf-8'))
server=service()
server.connections()

