"""
线程同步互斥锁
"""
from threading import Thread, Lock,Event
e = Event()
lock = Lock()

a = b = 1


def func01():
    while True:
        lock.acquire()
        if a != b:
            print(f"a={a},b={b}")
        lock.release()


t1 = Thread(target=func01)
t2 = Thread(target=func01)
t1.start()
t2.start()

while True:
    lock.acquire()
    a += 1
    b += 1
    lock.release()

t.join
