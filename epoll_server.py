"""
IO并发模型 基于epoll  tcp模型
"""

from socket import *
from select import *

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)
# 创建tcp套接字连接客户端
tcp_sock = socket()
tcp_sock.bind(ADDR)
tcp_sock.listen(5)

# 设置监控字典
dict01 = {tcp_sock.fileno():tcp_sock}

# 设置为非阻塞
tcp_sock.setblocking(False)

# 设置监听对象
ep = epoll()
ep.register(tcp_sock, EPOLLIN | EPOLLOUT)

while True:
    # 开始监听
    events = ep.poll()
    for item in events:
        if item[0] == tcp_sock.fileno():
            connfd, addr = tcp_sock.accept()
            print("connect from:", addr)
            connfd.setblocking(False)
            ep.register(connfd, EPOLLIN)
            dict01[connfd.fileno()] = connfd
        else:
            data = dict01[item[0]].recv(128)
            if not data:
                ep.unregister(dict01[item[0]])
                dict01[item[0]].close()
                del dict01[item[0]]
                continue
            print(data.decode())
            
            dict01[item[0]].send(b"OK")

