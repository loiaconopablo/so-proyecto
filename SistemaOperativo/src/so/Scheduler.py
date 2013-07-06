'''
@author: Pablo
'''
class SchedulerAbstract:

    def __init__(self, aPolicity, aKernel):
        if type(self) is SchedulerAbstract:
            raise NotImplementedError('Can\'t instantiate class `' + \cls.__name__ + '\';\n')
        else:
        #Cada politica guarda la lista de listos : self.qReady = []
            self.policity = aPolicity
            self.kernel = aKernel
        
    def next(self):
        if not self.isEmpty:
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
        if self.kernel.disk.isInDisk(aPCB.getNameProgram()):
            aPCB.setProgram(self.kernel.disk.get(aPCB.id))
            self.saveInMemory(aPCB)
            self.kernel.scheduler.add(aPCB)
        else:
            self.saveInMemory(aPCB)
            self.kernel.scheduler.add(aPCB)

    def saveInMemory(self, aPCB):
        if self.kernel.memory.isFreeBlockTo(aPCB):
            self.kernel.memory.saveInMemory(aPCB)
        else:
            self.add(aPCB)

    def checkForSpace(self):
        if self.hayWaiting():
            self.handle(self.policity.next)  
        
    def hayWaiting(self): 
        return len(self.policity.qReady) > 0    
