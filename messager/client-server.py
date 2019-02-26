from tkinter import *
from tkinter import filedialog, Frame
from socket import *
import urllib.request
from threading import Thread
from copy import copy
import time
import re
import pickle
from encryption.RSA import rsa
from encryption.AES import aes


class Interface(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="black")
        self.parent = parent
        self.user_name = 'Name'
        self.ip = urllib.request.urlopen('http://ip-address.ru/show').read().decode('utf-8')
        self.stack_msg = []
        self.server_flag = False  # is it a server?
        self.end_flag = False
        self.run_flag = False
        self.initUI()
        self.ex_crypto = Crypto(self.server_flag)

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

    def quit_(self, *args):
        print('000')
        self.end_flag = True
        self.parent.destroy()
        exit()

    def disconnect_(self, *args):
        self.insert_massage1('Disconnect')
        self.end_flag = True

    def change_user_name(self, *args):
        self.user_name = self.textFrame_name.get('1.0', END)

    def take_ip(self, *args):
        self.ip = self.textFrame_ip.get('1.0', END)

    def server_(self, ev):
        if self.run_flag:
            self.end_flag = True
        self.run_flag = True
        self.server_flag = True
        self.ex_crypto.ex_aes.generate_round_keys()
        Thread(target=Server, args=(ev, self), daemon=True).start()

    def client_(self, ev):
        if self.run_flag:
            self.end_flag = True
        self.run_flag = True
        Thread(target=Client, args=(ev, self), daemon=True).start()

    def send_massage1(self, *args):
        text = self.textFrame_cend.get('1.0', END)[:-1]
        self.insert_massage1('You:' + text + '\n')
        self.stack_msg.append(text)
        print('"' + text + '"')
        self.textFrame_cend.delete('1.0', END)

    def insert_massage1(self, text):
        self.textFrame.insert(END, text)


class Receive(Thread):
    """
    interface threading example
    """
    def __init__(self, obj, tcp_ser_sock=None):
        Thread.__init__(self)
        self.obj = obj
        self.tcpCliSock = obj.tcpCliSock
        self.BUFSIZ = obj.BUFSIZ
        self.interface = obj.interface
        if tcp_ser_sock:
            self.tcp_ser_sock = obj.tcp_ser_sock

    def session_initialization(self):
        """Сначала принимаем ник аппонента и обмениваемся
        открытыми ключами(RSA), для последующей передачи ключа шифрования AES."""
        data = self.tcpCliSock.recv(self.BUFSIZ)
        its_a_time = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        self.interface.ex_crypto.ex_rsa.open_key_other_user = pickle.loads(self.tcpCliSock.recv(self.BUFSIZ))
        if not self.interface.ex_crypto.ex_aes.ROUND_KEYS:
            len_of_keys_aes = self.tcpCliSock.recv(128)
            len_of_keys_aes = int(len_of_keys_aes.decode())
            time.sleep(0.2)
            fragments  = []
            while True:
                chunk = self.tcpCliSock.recv(1024)
                fragments.append(chunk)
                if fragments and len(b"".join(fragments)) == len_of_keys_aes:
                    break
            receiving_aes_key = pickle.loads(b"".join(fragments))
            self.interface.ex_crypto.ex_aes.ROUND_KEYS = self.interface.ex_crypto.ex_rsa.decrypt_massages(receiving_aes_key, self.interface.ex_crypto.ex_rsa.closed_key)
            self.interface.ex_crypto.ex_aes.ROUND_KEYS_COPY = copy(self.interface.ex_crypto.ex_aes.ROUND_KEYS)
        self.interface.insert_massage1('Connect' + '  ' + its_a_time + '  ' + data.decode('utf-8') + '\n')

    def run(self):
        self.session_initialization()
        while True and not self.interface.end_flag:
            try:
                data = pickle.loads(self.tcpCliSock.recv(self.BUFSIZ))
                print('res',data)
                its_a_time = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
                output = re.sub(r'(?<=\")[\'\x03\'][\x00]*', r'', (its_a_time + '  ' + bytes(self.interface.ex_crypto.decrypt(data)).decode('utf-8') + '\n'))
                print(output)
                self.interface.insert_massage1(output)
                if self.interface.end_flag:
                    self.tcpCliSock.close()
                    if self.tcp_ser_sock:
                        self.tcp_ser_sock.close()
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

    def session_initialization(self):
        self.tcpCliSock.send(self.interface.user_name.encode('utf-8'))
        self.tcpCliSock.send(pickle.dumps(self.interface.ex_crypto.ex_rsa.open_key))  # send self open key
        if self.interface.ex_crypto.ex_aes.ROUND_KEYS:
            time.sleep(0.3)
            encrypt_aes_round_key = self.interface.ex_crypto.ex_rsa.crypt_massages(self.interface.ex_crypto.ex_aes.ROUND_KEYS_COPY, self.interface.ex_crypto.ex_rsa.open_key_other_user)
            self.tcpCliSock.send(str(len(pickle.dumps(encrypt_aes_round_key))).encode())
            self.tcpCliSock.send(pickle.dumps(encrypt_aes_round_key))  # send encrypt round key AES

    def run(self):
        """Запуск потока"""
        self.session_initialization()
        while True and not self.interface.end_flag:
            if self.interface.stack_msg:
                formating_message = self.interface.ex_crypto.encrypt(('[' + self.interface.user_name + '] "' + self.interface.stack_msg.pop() + '"').encode('utf-8') + b'\x03')
                print('out', formating_message)
                self.tcpCliSock.send(pickle.dumps(formating_message))
            time.sleep(0.5)
            if self.interface.end_flag:
                self.tcpCliSock.close()




class Client:
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
        r = Receive(self)
        # r.setDaemon(False)
        r.start()
        ex_input = Input(self)
        # ex_input.setDaemon(False)
        ex_input.start()
        r.join()
        ex_input.join()


def create(self, interface):
    self.interface = interface
    self.interface.end_flag = False
    self.ip = '0.0.0.0'  # адрес хоста (сервера) пустой означает использование любого доступного адреса
    self.PORT = 8080  # номер порта на котором работает сервер (от 0 до 65525, порты до 1024 зарезервированы для системы, порты TCP и UDP не пересекаются)
    self.BUFSIZ = 1024  # размер буфера 1Кбайт
    self.user_name = interface.user_name
    self.ADDR = (self.ip, self.PORT)  # адрес сервера
    self.tcp_ser_sock = socket(AF_INET, SOCK_STREAM)  # создаем сокет сервера
    self.tcp_ser_sock.bind(self.ADDR)
    self.tcp_ser_sock.listen(5)
    self.tcpCliSock, self.addr = self.tcp_ser_sock.accept()


class Server:

    def __init__(self, ev, interface):
        thread1 = Thread(target=create, args=(self, interface))
        thread1.start()
        thread1.join()
        self.create_threads()

    def create_threads(self):
        """
        Создаем группу потоков
        """
        r = Receive(self, tcp_ser_sock=self.tcp_ser_sock)
        r.start()
        ex_input = Input(self)
        ex_input.start()
        r.join()
        ex_input.join()


class Crypto:
    def __init__(self, server_flag):
        """При инициалищации генерирует ключи AES и RSA."""
        self.ex_aes = aes(server_flag)
        self.ex_rsa = rsa()
        print(self.ex_rsa.open_key, self.ex_rsa.closed_key)

    def encrypt(self, message_data):
        """Принимает сообщение и шифрует его шифром AES"""
        code_data = self.ex_aes.crashing_message(message_data)
        for i in code_data:
            self.ex_aes.coding(i, 10)
        message_data = self.ex_aes.connect_massage(code_data)
        return message_data

    def decrypt(self, message_data):
        """Принимает сообщение и дешифрует его шифром AES"""
        code_data = self.ex_aes.crashing_message(message_data)
        for i in code_data:
            self.ex_aes.decoding(i, 10)
        message_data = self.ex_aes.connect_massage(code_data)
        return message_data


def main():
    # c = Crypto(True)
    # mass = [1,2,3,0,0,0,0,0,0,0,0,0,0,0,]
    # print(c.decrypt(c.encrypt(mass)))

    root = Tk()
    root.geometry("600x600+1100+300")
    app = Interface(root)
    app.mainloop()


if __name__ == '__main__':
    main()
