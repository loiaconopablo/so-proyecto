'''
@author: Pablo
'''
import threading
semaforo = threading.Semaphore()

class Fifo:

    def __init__(self):
        self.qReady = []

    def next(self):
        semaforo.acquire()
        return self.qReady.pop(0)
        semaforo.release()
        
    def add(self, aPCB):
        semaforo.acquire()
        return self.qReady.append(aPCB)
        semaforo.release()
        
    def isRR(self):
        return False
    
    def retryAdd(self, aPCB):
        semaforo.acquire()
        self.add(aPCB)
        semaforo.release()