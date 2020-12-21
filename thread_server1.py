"""
- 创建网络套接字用于接收客户端请求
- 等待客户端连接
- 客户端连接，则创建新的线程具体处理客户端请求
- 主线程继续等待其他客户端连接
- 如果客户端退出，则销毁对应的线程
"""
import sys
from threading import Thread
from socket import *

# 客户线程类：
class ClientThread(Thread):
    def __init__(self,connfd,daemon = True):
        super().__init__()
        self.connfd = connfd
    def run(self):
        while True:
            data = self.connfd.recv(1024)
            if not data:
                break
            print(data.decode())
        self.connfd.close()


# 创建服务类
class TheardServer:
# 定义常规变量
    HOST = "0.0.0.0"
    POST = 8888
    ADDR = (HOST,POST)
    def __init__(self):
        self.tcp_socket = socket(AF_INET, SOCK_STREAM)
        self.tcp_socket.bind(TheardServer.ADDR)
        self.tcp_socket.listen(5)

    # def handle(self,connfd):
    #     while True:
    #         data = connfd.recv(1024)
    #         if not data:
    #             break
    #         print(data.decode())
    #     connfd.close()

    def main(self):
        while True:
            try:
                connfd,addr = self.tcp_socket.accept()
                print("Connect from:",addr)
            except KeyboardInterrupt:
                self.tcp_socket.close()
                sys.exit("结束服务")
            t = ClientThread(target=self.handle,args=(connfd,),daemon=True)
            t.start()

if __name__ == '__main__':
    server = TheardServer()
    server.main()