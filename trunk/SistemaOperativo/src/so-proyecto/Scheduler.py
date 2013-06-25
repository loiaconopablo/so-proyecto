'''
@author: Pablo
'''
from Fifo import *
from RoundRobin import *
from Priority import *
from FifoWithRR import *
from PriorityWithRR import *

class SchedulerAbstract:

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
        self
        
    def retryAdd(self, aPCB):
        self

    def isEmpty(self):
        return len(self.policity.qReady) == 0
    
    def quamtum(self):
        if self.policity.isRR():
            return self.policity.getQuantum()
        else: return 10

class ShortScheduler(SchedulerAbstract):
    def __init__(self, SchedulerAbstract, aPolicity, aKernel):
        SchedulerAbstract.__init__(self, aPolicity, aKernel)
       
    def add(self, aPCB):
        aPCB.changeStatus(State.READY)
        self.policity.add(aPCB)
        
    def retryAdd(self, aPCB):
        aPCB.changeStatus(State.READY)
        self.policity.retryAdd(aPCB) 
        
class LongScheduler(SchedulerAbstract):
    
    def __init__(self, SchedulerAbstract, aPolicity, aKernel):
        SchedulerAbstract.__init__(self, aPolicity, None)
        
    def add(self, aPCB):
        aPCB.changeStatus(State.WAITING)
        self.policity.add(aPCB)
        
    def retryAdd(self, aPCB):
        aPCB.changeStatus(State.WAITING)
        self.policity.retryAdd(aPCB)

    def handle(self, aPCB):
        aPCB.setProgram(self.kernel.disk.get(aPCB.id))
        if self.kernel.memory.isFreeBlockTo(aPCB):
            self.kernel.memory.saveInMemory(aPCB)
        else:
            self.add(aPCB)

    def checkForSpace(self): #Verificar si es necesario
        if self.hayWaiting():
            self.handle(self.colaWait.pop(0))
        
    def hayWaiting(self): #Verificar
        return len(colaWait)>0    

