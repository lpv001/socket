import socket 
from _thread import *

s = socket.socket()
HOST = 'localhost'
PORT = 8888

print("Waiting for connection response")
user = input('Input name: ')
print("--------------")


try:
    s.connect((HOST, PORT))
    s.send(f"{user} Joined Chatroom".encode('utf-8'))
except socket.error as e:
    print(str(e))

def receive_message(connection):
    res = connection.recv(1024)
    data = repr(res.decode('utf-8'))
    print('\n--------------')
    print('server message: ' + data)
    print('--------------')

def send_message(connection):
    Input = input('Send message: ')
    connection.send(f'User: {user}, Message: {Input}'.encode('utf-8'))

while True:
    Input = input('Send message: ')
    if (Input != ""):
        s.send(f'User: {user}, Message: {Input}'.encode('utf-8'))
        print('--------------')
    # if (s.recv(1024)):
    #     print("hello")
    # res = s.recv(1024)
    # data = repr(res.decode('utf-8'))
    # print('--------------')
    # print(data)
    # print('--------------')
    start_new_thread(receive_message, (s,))

