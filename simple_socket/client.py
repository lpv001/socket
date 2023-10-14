import socket 

HOST = '172.18.18.95'
PORT = 8888

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.connect((HOST ,PORT))
    s.sendall('Hello gic'.encode('utf8'))
    data = s.recv(1024).decode('utf8')
    print('Sent', repr(data))