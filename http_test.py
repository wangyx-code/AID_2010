"""
获取http请求和响应
"""
from socket import *

tcp_sock = socket(AF_INET,SOCK_STREAM)
tcp_sock.bind(("0.0.0.0",8888))
tcp_sock.listen(5)

connfd,addr = tcp_sock.accept()
print("连接地址：",addr)

data = connfd.recv(1024*10)
print(data.decode())

# 发送响应
response = """HTTP/1.1 200 OK
Content-Type:text/html;charset=UTF-8

hello 小泽
"""
connfd.send(response.encode())

connfd.close()
tcp_sock.close()