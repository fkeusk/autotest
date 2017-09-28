import socket,threading
from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys
class clients(QWidget):
    def __init__(self):
        self.cc = socket.socket()
        self.host='localhost'
        self.port=555
        self.coninfo=(self.host,self.port)
        self.cc.connect(self.coninfo)
        # print(self.cc.recv(1024).decode('utf-8'))
        QtGui,QWidget.__init__(self)
        self.setGeometry(500, 300, 400, 400)
        self.setWindowTitle("Login")
        self.addUI()

    def addUI(self):
        labe = QLabel('无聊聊天室',self)
        labe.setGeometry(145,200,300,30)
        labe.setFont(QFont('微软雅黑',18,QFont.Bold))
        #labe.setText("<font color=%s>%s</font>" %("gred",'XXXX管理系统'))  设置字体颜色
        lab3 = QLabel('聊天内容',self)
        lab3.setFont(QFont('微软雅黑',15))
        lab3.setGeometry(160,5,300,30)
        self.text3 = QTextBrowser(self)
        self.text3.setGeometry(10,40,380,160)

        lab1 = QLabel('输入昵称：',self)
        lab1.setFont(QFont('微软雅黑',12,QFont.Bold))
        lab1.setGeometry(10,240,90,30)
        text = QLineEdit(self)
        text.setGeometry(110,240,150,30)
        self.input = text
        # self.setLayout(grid)
        button = QPushButton('进入',self)
        button.setFont(QFont('微软雅黑',10,QFont.Bold))
        button.setGeometry(270,240,60,30)
        self.butt = button
        self.butt.clicked.connect(self.sendname)
        t2=threading.Thread(target=self.recieves)
        t2.start()
        lab2 = QLabel('输入框:',self)
        lab2.setFont(QFont('微软雅黑',14))
        lab2.setGeometry(10,270,100,30)
        self.tex = QTextEdit(self)
        self.tex.setGeometry(10,300,380,65)

        button = QPushButton('发送',self)
        button.setFont(QFont('微软雅黑',10,QFont.Bold))
        button.setGeometry(320,370,60,30)
        self.button = button
        self.button.clicked.connect(self.sends)


    def sendname(self):
        self.cc.send(self.input.text().encode('utf-8'))
        self.butt.clicked.disconnect(self.sendname)
        # print(self.cc.recv(1024).decode('utf-8'))

    def sends(self):
        self.cc.send((self.tex.toPlainText()).encode('utf-8'))
        self.tex.clear()
    def recieves(self):
        while 1:
            chats=self.cc.recv(1024).decode('utf-8')
            self.text3.append(chats)
app=QApplication(sys.argv)
client=clients()

client.show()
sys.exit(app.exec())

        # print(cc.recv(1024).decode('utf-8'))
