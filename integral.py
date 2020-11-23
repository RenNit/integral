import math
import threading
from threading import Thread
import _thread as thread
import time
import queue
from string import ascii_lowercase
import itertools

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):

        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return

class Integral:
    def f(self, x):
        self.x = x
        return 1/(math.pi + math.sin(x))
    def calc(self, a, b):
        self.a = a
        self.b = b
        s = 0
        h = 0.000001
        x = a + h
        while(x <= (b - h)):
            s += 2 * self.f(x)
            x += h
        s += self.f(a)
        s += self.f(b)
        return s * h / 2
        
sec = Integral()
def threads(n):
    step = (2 * math.pi) / n
    a = -math.pi
    value = 0
    lst = []
    for i in range (0, n):
        lst.append(i)
        b = a + step
        lst[i] = ThreadWithReturnValue(target=sec.calc, args=(a, b))
        lst[i].start()
        a = b
    for i in range(0, n):
        lst.append(i)
        value += lst[i].join()
    return value

for i in range (1, 11):
    print (i)
    start_time = time.time()
    print(threads(i))
    print("--- %s секунд ---" % (time.time() - start_time))
