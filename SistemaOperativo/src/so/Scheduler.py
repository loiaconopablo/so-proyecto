'''
@author: Pablo
'''
from State import *
from Kernel import *

class SchedulerAbstract:

    def __init__(self, aPolicity, aKernel):
        if type(self) is SchedulerAbstract:
            raise NotImplementedError('Can\'t instantiate class ')
        else:
        #Cada politica guarda la lista de listos : self.qReady = []
            self.policity = aPolicity
            self.kernel = aKernel
        
    def next(self):
        if not self.isEmpty():
            return self.policity.next()
        else:
            self.kernel.manageIRQ.nilInterrupt()
    
    def add(self, aPCB):
        pass
        
    def retryAdd(self, aPCB):
        pass

    def isEmpty(self):
        return len(self.policity.qReady) == 0
    
    def quamtum(self):
        if self.policity.isRR():
            return self.policity.getQuantum()
        else: return 10

class ShortScheduler(SchedulerAbstract):
    def __init__(self, aPolicity, aKernel):     
        SchedulerAbstract.__init__(self, aPolicity, aKernel)
       
    def add(self, aPCB):
        aPCB.changeStatus(State.READY)
        self.policity.add(aPCB)
        
    def retryAdd(self, aPCB):
        aPCB.changeStatus(State.READY)
        self.policity.retryAdd(aPCB) 
        
class LongScheduler(SchedulerAbstract):
    
    def __init__(self, aPolicity, aKernel):
        SchedulerAbstract.__init__(self, aPolicity, aKernel)
        
    def add(self, aPCB):
        aPCB.changeStatus(State.WAITING)
        self.policity.add(aPCB)
        
    def retryAdd(self, aPCB):
        aPCB.changeStatus(State.WAITING)
        self.policity.retryAdd(aPCB)

    def saveInMemory(self, aPCB):
        if (self.kernel.mmu.freeSize() >= aPCB.getSize()):
            self.kernel.mmu.saveInMemory(aPCB)
            self.kernel.shortScheduler.add(aPCB)
        else:
            self.add(aPCB)

    def handle(self, aPCB):
        if self.kernel.disk.isInDisk(aPCB.getNameProgram()):
            aPCB.setProgram(self.kernel.disk.get(aPCB.getNameProgram()))
            aPCB.setPriority(aPCB.id.priority)
            self.saveInMemory(aPCB)
        else:
            self.kernel.manageIRQ.noFoundProgram(aPCB.getNameProgram())

    def checkForSpace(self):
        if self.hayWaiting():
            self.handle(self.policity.next())  
        
    def hayWaiting(self): 
        return len(self.policity.qReady) > 0    
