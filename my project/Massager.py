import socket
from copy import copy
from AES import KeyExpansionAES, Genarate_keys, Crypt_massages, Coding, CrashingMassage, ConnectMassage, DeCoding
import _pickle
import select
import threading
from time import sleep


RaundKeysAES = KeyExpansionAES()

open_key_server, closed_key_server = Genarate_keys()
RaundKeys_copy = copy(RaundKeysAES)

Massage_data='6dn54b54kb54iobu45oh0hb40'.encode('utf-8')
def Encrypt(Massage_data, RaundKeys):
    Code_data=CrashingMassage(Massage_data)
    for iter in Code_data:
        Coding(iter, RaundKeys, 10)
    Massage_data = ConnectMassage(Code_data)
    return Massage_data

def Decrypt(Massage_data, RaundKeys):
    Code_data=CrashingMassage(Massage_data)
    for iter in Code_data:
        DeCoding(iter, RaundKeys, 10)
    Massage_data = ConnectMassage(Code_data)
    return Massage_data

def BeginSession():
    conn.send(_pickle.dumps(open_key_server, 2))
    open_key_client = _pickle.loads(conn.recv(1024))
    Crypt_key_AES = Crypt_massages(RaundKeys_copy, open_key_client)
    conn.sendall(_pickle.dumps(Crypt_key_AES, 2))
    #conn.recv(1024)

def SendMassage(RaundKeys):
    massage = _pickle.dumps(input("Pleas: "), 2)
    conn.sendall(_pickle.dumps(Encrypt(massage, RaundKeys), 2))
    #conn.recv(1024)
def GetMassage(RaundKeysAES):
    conn.settimeout(60)
    mas = conn.recv(1024)
    #sleep(30)

    if not mas:  # сокет закрыли, пустой объект
        return
    massage = Decrypt(_pickle.loads(mas), RaundKeysAES)
    print(_pickle.loads(bytes(massage)))

sock = socket.socket()
sock.bind(("", 14902))
sock.listen(10)
conn, addr = sock.accept()
print(conn, addr)
sock.setblocking(0)
BeginSession()
sock.settimeout(0.2)
#SendMassage(RaundKeysAES)

def writer(RaundKeysAES, event_for_wait, event_for_set, conn):
    event_for_wait.wait() # wait for event
    event_for_wait.clear() # clean event for future
    #r, _, _ = select.select([conn], [], [])
    #print(r)
    #if r:
    #    GetMassage(RaundKeysAES)

    GetMassage(RaundKeysAES)
    event_for_set.set()
def writer1(RaundKeysAES, event_for_wait, event_for_set):
    event_for_wait.wait() # wait for event
    event_for_wait.clear() # clean event for future
    SendMassage(RaundKeysAES)
    event_for_set.set()
# init events
while True:
    e1 = threading.Event()
    e2 = threading.Event()

    # init threads

    t1 = threading.Thread(target=writer1, args=(RaundKeysAES, e1, e2))
    t2 = threading.Thread(target=writer, args=(RaundKeysAES, e2, e1,conn))

    # start threads
    t1.start()
    t2.start()

    e1.set() # initiate the first event

    # join threads to the main thread
    t1.join()
    t2.join()

#
# while True:
#     while True:
#         r, _, _ = select.select([conn],[],[])
#         if r:
#             GetMassage(RaundKeysAES)
#         break
#
#     SendMassage(RaundKeysAES)
#
#     SendMassage(RaundKeysAES)
#

# data = conn.recv(16384)
# udata = data.decode("utf-8")
# print(udata)
# tmp = conn.recv(1024)
# data = b""
# utmp = tmp.decode("utf-8")
# print(utmp)
# while 1:
#     tmp = conn.recv(1024)
#     data = tmp
#     # while tmp:
#     #    data+=tmp
#     #    tmp=conn.recv(1024)
#     gas = data.decode("utf-8")
#     data = b""
#     print(gas)
#     if gas == 'exi':
#         break
#
# print("Data: " + udata)
# conn.send(b"Hello!\n")
# conn.send(b"your data: " + udata.encode("utf-8"))
# conn.send('exi'.encode("utf-8"))
conn.close()
