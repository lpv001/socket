import socket
from _thread import *

#create initial socket
s = socket.socket()
# bos server
HOST = 'localhost'  
PORT = 8888
ThreadCount = 0

try:
    s.bind((HOST,PORT))
except socket.error as e:
    print(str(e))

s.listen(5)

def multi_threaded_client(connection):
    while True:
        data = connection.recv(2048)
        if not data:
            break
        message =  repr(data.decode('utf-8'))
        # connection.sendall(str.encode(message))
        print(message)
        print('----------------')
    connection.close()
    
def send_message_threaded_client(connection):
    while True:
        message = input()
        if message != "":
            connection.sendall(str.encode(message))
            print('----------------')
            print('message from server: ' + message)
            print('----------------')
    
while True:
    print('Server is listening in port ' + str(PORT))
    Client, address = s.accept()
    print('\nConnected from: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client,(Client, ))
    print('Thread Number: ' + str(ThreadCount))
    start_new_thread(send_message_threaded_client,(Client, ))
    ThreadCount += 1
    


