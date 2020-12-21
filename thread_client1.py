"""
并发线程客户端
"""
from socket import *

ADDR = ("127.0.0.1",8888)
tcp_socket = socket()
tcp_socket.connect(ADDR)
while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())
tcp_socket.close()