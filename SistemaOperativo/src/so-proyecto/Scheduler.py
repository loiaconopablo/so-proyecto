'''
@author: Pablo
'''
from Fifo import *
from RoundRobin import *
from Priority import *
from FifoWithRR import *
from PriorityWithRR import *

class Scheduler:

    def __init__(self, aPolicity, aKernel):
       #Cada politica guarda la lista de listos : self.qReady = []
        self.policity = aPolicity
        self.kernel = aKernel
        
    def next(self):
        if not self.isEmpty:
            return self.policity.next()
        else:
            self.kernel.manageIRQ.nilInterrupt()

    def add(self, aPCB):
        aPCB.changeStatus(State.READY)
        self.policity.add(aPCB)
        
    def retryAdd(self, aPCB):
        aPCB.changeStatus(State.READY)
        self.policity.retryAdd(aPCB)

    def isEmpty(self):
        return len(self.policity.qReady) == 0
    
    def quamtum(self):
        if self.policity.isRR():
            return self.policity.getQuantum()
        else: return 10
        
    

