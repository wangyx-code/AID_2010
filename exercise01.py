"""
利用阻塞控制对共享资源的使用
联系：两个线程：一个打印1---52    一个打印A---Z
要求两个线程一起执行，打印顺序为12A34B........5152Z
"""
from threading import Thread,Lock,Event
lock1 = Lock()
lock2 = Lock()
e = Event()

def func01():
    for i in range(65,91):
        lock1.acquire()
        print(chr(i))
        lock2.release()


def func02():
    for j in range(1,53,2):
        lock2.acquire()
        print(j,j+1)
        lock1.release()



t1 = Thread(target=func01)
t2 = Thread(target=func02)
lock1.acquire()
t1.start()
t2.start()
t1.join()
t2.join()

