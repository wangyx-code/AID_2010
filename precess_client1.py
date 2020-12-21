from socket import *

ADDR = ("127.0.0.1",8888)
tcp_socket = socket(AF_INET,SOCK_STREAM)
tcp_socket.connect(ADDR)

while True:
    msg = input(">>")
    tcp_socket.send(msg.encode())
    if not msg:
        break
tcp_socket.close()
