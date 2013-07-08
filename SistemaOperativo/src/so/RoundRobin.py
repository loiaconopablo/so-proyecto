'''
@author: Pablo
'''
import threading
semaforo = threading.Semaphore()

class RoundRobin:

    def __init__(self, aQuantum):
        self.quantum = aQuantum  
        self.qReady = []

    def next(self):
        semaforo.acquire()
        return self.qReady.pop(0)
        semaforo.release()

    def add(self, aPCB):
        semaforo.acquire()
        self.qReady.append(aPCB)
        return self.qReady
        semaforo.release()
        
    def retryAdd(self, aPCB):
        self.add(aPCB)
    
    def isRR(self):
        return True
    
    def getQuantum(self):
        return self.quantum

