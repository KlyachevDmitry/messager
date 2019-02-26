from tkinter import *
from tkinter import filedialog, Frame
from socket import *
import urllib.request
from threading import Thread

import time


class Interface(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="black")
        self.parent = parent
        self.user_name = 'Name'
        self.ip = urllib.request.urlopen('http://ip-address.ru/show').read().decode('utf-8')
        self.stack_msg = []
        self.end_flag = False
        self.run_flag = False
        self.initUI()

    def initUI(self):

        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)
        self.quit = Button(self.parent, text='quit')
        self.quit.bind("<Button-1>", self.quit_)
        self.quit.place(x=560, y=0, width=40, height=40)

        self.textFrame = Text(self.parent, height=200, width=200, font='Arial 14', wrap=WORD)
        self.scrollbar = Scrollbar(self.textFrame)
        self.scrollbar['command'] = self.textFrame.yview
        self.textFrame['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.pack(side='right', fill='y')
        self.textFrame.place(x=0, y=90, width=600, height=510)

        self.textFrame_cend = Text(self.parent, font='Arial 14', wrap=WORD)
        self.textFrame_cend.place(x=0, y=500, width=550, height=100)
        self.textFrame_cend['bg'] = 'grey'

        self.textFrame_ip = Text(self.parent, font='Arial 12', wrap=WORD)
        self.textFrame_ip.place(x=0, y=0, width=120, height=40)
        self.textFrame_ip.insert(1.0, self.ip)

        self.textFrame_name = Text(self.parent, height=20, width=200, font='Arial 12', wrap=WORD)
        self.textFrame_name.place(x=0, y=40, width=120, height=40)
        self.textFrame_name.insert(1.0, self.user_name)

        self.disconnect = Button(self.parent, text='Disconnect')
        self.disconnect['bg'] = 'yellow'
        self.disconnect.bind('<Button-1>', self.disconnect_)
        self.disconnect.place(x=200, y=0, width=100, height=40)

        self.send_massage = Button(self.parent, text='Send')
        self.send_massage['bg'] = 'red'
        self.send_massage.bind('<Button-1>', self.send_massage1)
        self.send_massage.place(x=550, y=500, width=50, height=100)

        self.apply_ip = Button(self.parent, text='apply ip')
        self.apply_ip['bg'] = 'green'
        self.apply_ip.bind('<Button-1>', self.take_ip)
        self.apply_ip.place(x=120, y=0, width=80, height=40)

        self.apply_name = Button(self.parent, text='apply name')
        self.apply_name['bg'] = 'green'
        self.apply_name.bind('<Button-1>', self.change_user_name)
        self.apply_name.place(x=120, y=40, width=80, height=40)

        self.serv = Button(self.parent, text='Server')
        self.serv['bg'] = 'green'
        self.serv.bind('<Button-1>', self.server_)
        self.serv.place(x=300, y=0, width=120, height=40)

        self.clint = Button(self.parent, text='Client')
        self.clint['bg'] = 'green'
        self.clint.bind('<Button-1>', self.client_)
        self.clint.place(x=420, y=0, width=120, height=40)

    def quit_(self, ev):
        print('000')
        self.end_flag = True
        self.parent.destroy()
        exit()

    def disconnect_(self, ev):
        self.insert_massage1('Disconnect')
        self.end_flag = True

    def change_user_name(self, ev):
        self.user_name = self.textFrame_name.get('1.0', END)

    def take_ip(self, ev):
        self.ip = self.textFrame_ip.get('1.0', END)

    def server_(self, ev):
        if self.run_flag == True:
            self.end_flag = True
        self.run_flag = True
        Thread(target=server, args=(ev, self), daemon=True).start()

    def client_(self, ev):
        if self.run_flag == True:
            self.end_flag = True
        self.run_flag = True
        Thread(target=client, args=(ev, self), daemon=True).start()

    def send_massage1(self, ev):
        text = self.textFrame_cend.get('1.0', END)[:-1]
        self.insert_massage1('You:' + text + '\n')
        self.stack_msg.append(text)
        print('"' + text + '"')
        self.textFrame_cend.delete('1.0', END)

    def insert_massage1(self, text):
        self.textFrame.insert(END, text)


class resive(Thread):
    """
    interface threading example
    """

    def __init__(self, obj, tcpSerSock=None):
        Thread.__init__(self)
        self.obj = obj
        self.tcpCliSock = obj.tcpCliSock
        self.BUFSIZ = obj.BUFSIZ
        self.interface = obj.interface
        if tcpSerSock:
            self.tcpSerSock = obj.tcpSerSock

    def run(self):
        """Запуск потока"""
        data = self.tcpCliSock.recv(self.BUFSIZ)
        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        self.interface.insert_massage1('Connect' + '  ' + itsatime + '  ' + data.decode('utf-8') + '\n')

        while True and self.interface.end_flag == False:
            try:
                data = self.tcpCliSock.recv(self.BUFSIZ)
                itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
                print(data.decode('utf-8'))
                self.interface.insert_massage1(itsatime + '  ' + data.decode('utf-8') + '\n')
                if self.interface.end_flag == True:
                    self.tcpCliSock.close()
                    if self.tcpSerSock:
                        self.tcpSerSock.close()
            except ConnectionAbortedError:
                self.interface.disconnect_("")
                self.end_flag = False
                print('An established connection was aborted by the software in your host machine')
            except ConnectionResetError:
                self.interface.disconnect_("")
                self.end_flag = False
                print('[WinError 10054] An existing connection was forcibly closed by the remote host')


class Input(Thread):
    """
    interface threading example
    """

    def __init__(self, obj):
        """Инициализация потока"""
        Thread.__init__(self)
        self.obj = obj
        self.tcpCliSock = obj.tcpCliSock
        self.BUFSIZ = obj.BUFSIZ
        self.interface = obj.interface

    def run(self):
        """Запуск потока"""
        self.tcpCliSock.send(self.interface.user_name.encode('utf-8'))
        while True and self.interface.end_flag == False:
            if self.interface.stack_msg:
                self.tcpCliSock.send(('[' + self.interface.user_name + ']' + '  ' + self.interface.stack_msg.pop()).encode('utf-8'))
            time.sleep(0.5)
            if self.interface.end_flag == True:
                self.tcpCliSock.close()


class client():
    def __init__(self, ev, interface):
        self.flag_server = False
        self.interface = interface
        self.interface.end_flag = False
        self.ip = urllib.request.urlopen('http://ip-address.ru/show').read().decode('utf-8')

        # self.ip = '127.0.0.1'
        self.user_name = interface.user_name

        self.PORT = 8080

        self.BUFSIZ = 1024

        self.ADDR = (self.ip, self.PORT)

        self.tcpCliSock = socket(AF_INET, SOCK_STREAM)

        self.tcpCliSock.connect(self.ADDR)  # установка связи с сервером

        self.create_threads()

    def create_threads(self):
        """
        Создаем группу потоков
        """
        R = resive(self)
        # R.setDaemon(False)
        R.start()
        I = Input(self)
        # I.setDaemon(False)
        I.start()
        R.join()
        I.join()


def create(self, interface):
    self.interface = interface
    self.interface.end_flag = False

    self.ip = '0.0.0.0'  # адрес хоста (сервера) пустой означает использование любого доступного адреса
    self.PORT = 8080# номер порта на котором работает сервер (от 0 до 65525, порты до 1024 зарезервированы для системы, порты TCP и UDP не пересекаются)

    self.BUFSIZ = 1024  # размер буфера 1Кбайт

    self.user_name = interface.user_name
    self.ADDR = (self.ip, self.PORT)  # адрес сервера
    self.tcpSerSock = socket(AF_INET, SOCK_STREAM)  # создаем сокет сервера
    self.tcpSerSock.bind(self.ADDR)
    self.tcpSerSock.listen(5)
    self.tcpCliSock, self.addr = self.tcpSerSock.accept()


class server():

    def __init__(self, ev, interface):
        thread1 = Thread(target=create, args=(self, interface))
        thread1.start()
        thread1.join()
        self.create_threads()

    def create_threads(self):
        """
        Создаем группу потоков
        """
        R = resive(self, tcpSerSock=self.tcpSerSock)
        # R.setDaemon(False)
        R.start()
        I = Input(self)
        # I.setDaemon(False)
        I.start()
        R.join()
        I.join()


def main():
    root = Tk()
    root.geometry("600x600+1100+300")
    app = Interface(root)
    app.mainloop()


if __name__ == '__main__':
    main()
