'''
Created on 30/05/2013

@author: Pablo Loiacono
'''
from Kernel import *
from Disk import *
from Memory import *
from State import *
from PCB import *
from Scheduler import *

class LongScheduler:
    
    def __init__(self,aKernel, aPolicity):
        self.kernel = aKernel
        self.scheduler = Scheduler(aPolicity, aKernel)
        
    def handle(self, aPCB):
        aPCB.setProgram(self.kernel.disk.get(aPCB.id))
        if self.kernel.memory.isFreeBlockTo(aPCB):
            self.kernel.memory.saveInMemory(aPCB)
        else:
            aPCB.changeStatus(State.WAITING)
            self.scheduler.add(aPCB)
                        
    def checkForSpace(self):
        if self.hayWaiting():
            self.handle(self.colaWait.pop(0))
        
    def hayWaiting(self):
        return len(colaWait)>0