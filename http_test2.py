"""
HTTP协议
将一个文件内容作为响应体，发送给浏览器显示
"""
from socket import *

tcp_sock = socket()
tcp_sock.bind(("0.0.0.0",8888))
tcp_sock.listen(5)

connfd,addr = tcp_sock.accept()
data = connfd.recv(128)

# 发送响应
file = open("timg.jpg","rb")
data = file.read()
response = """HTTP/1.1 200 OK
Content-Type:image/jpg

"""
response = response.encode()+data
connfd.send(response)
file.close()
connfd.close()
tcp_sock.close()

