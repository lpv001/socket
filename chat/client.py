import socket 

s = socket.socket()
HOST = '172.18.18.95'
PORT = 8889

print("Waiting for connection response")
user = input('Input name: ')
print("--------------")

try:
    s.connect((HOST, PORT))
    s.send(f"{user} Joined Chatroom".encode('utf-8'))
except socket.error as e:
    print(str(e))

while True:
    Input = input('Send message: ')
    s.send(f'User: {user}, Message: {Input}'.encode('utf-8'))
    res = s.recv(1024)
    print('--------------')
    print(res)

    

