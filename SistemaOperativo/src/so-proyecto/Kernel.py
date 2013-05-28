'''
@author: Pablo
'''

from Scheduler.py import *

class Kernel:

    def __init__(self,cpu,policity,aMemory):

        self.processor = cpu
        self.modeKernel = False #comienza en modo usuario
        self.scheduler = Scheduler(policity)
        # self.pcbCurrent
        self.handlerIO = HandlerIO()
        self.memory = aMemory
        self.timer = Timer(self) 
        self.pcbFinish = []
        self.manageIRQ = ManageIRQ(self)
        
    #def run(self):

    def modeOn(self):#lo pone en modo kernel
        self.modeKernel = True  

    def modeOff(self):#lo pone en modo usuario
        self.modeKernel = False
        
    def setNextPcb(self):
        return self.cpu.setPcb(self.scheduler.next())

    def contextSwitch(self):
        if self.cpu.pcbCurrent == null: ##chequeo si el CPU finalizo el ultimo PCB o lo 
            self.setNextPcb() ##  seteo en el pcb del CPU el proximo pcb
        else:
            self.scheduler.add(self.cpu.pcbCurrent) ## vuelvo a poner el pcb en la cola qReady
            self.setNextPcb() ##  seteo en el pcb del CPU el proximo pcb
            
    def isModeKernel(self):
        return self.modeKernel