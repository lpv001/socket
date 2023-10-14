import socket

# bos server
HOST = '172.18.18.95'  
PORT = 8888
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print(f'Server is running on port {PORT}')
        s.listen()
        conn, addr = s.accept()
        with conn:
                print('Connected by', addr)
                while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        conn.sendall(data)
                        print('Received', repr(data.decode('utf8')))