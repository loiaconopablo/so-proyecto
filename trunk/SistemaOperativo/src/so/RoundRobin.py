'''
@author: Pablo
'''
#===============================================================================
# import threading       NO FUE NECESARIO
# semaforo = threading.Lock()  
#===============================================================================


class RoundRobin:

    def __init__(self, aQuantum):
        self.quantum = aQuantum  
        self.qReady = []

    def next(self):
        return self.qReady.pop(0)

    def add(self, aPCB):
        self.qReady.append(aPCB)
        return self.qReady
        
    def retryAdd(self, aPCB):
        self.add(aPCB)
    
    def isRR(self):
        return True
    
    def getQuantum(self):
        return self.quantum

