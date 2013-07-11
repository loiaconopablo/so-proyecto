'''
@author: Pablo
'''

from Scheduler import *
from CPU import *
from ManageIRQ import *
from MMU import *
from PCB import *
from Timer import *



class Kernel:

    def __init__(self, policity, aMMU, aDisk):
        self.modeKernel = False  # comienza en modo usuario
        self.mmu = aMMU
        self.pcbFinish = []
        self.disk = aDisk
        self.manageIRQ = ManageIRQ(self)     
        self.handlerIO = HandlerIO(self.manageIRQ)
        self.shortScheduler = ShortScheduler(policity, self)
        self.longScheduler = LongScheduler(policity, self)#revisar
        self.cpu = CPU(self)
           
    def initializeThread(self):
        self.cpu.initializeThread()
        self.handlerIO.initializeThread()
           
    def modeOn(self):  # lo pone en modo kernel
        self.modeKernel = True  

    def modeOff(self):  # lo pone en modo usuario
        self.modeKernel = False
        
    def setNextPcb(self):
        self.cpu.setPCB(self.shortScheduler.next())
        self.cpu.timer.reset()

    def contextSwitch(self):
        self.modeOn() # coloco en modo kernel
        if self.cpu.pcbCurrent == None:  # #chequeo si el CPU finalizo el ultimo PCB o lo 
            self.setNextPcb()            # #  seteo en el pcb del CPU el proximo pcb
        else:
            self.returnToPcbTable()  # # vuelvo a poner el pcb en la cola qReady
            self.setNextPcb()  # #  seteo en el pcb del CPU el proximo pcb
        self.modeOff() #vuelvo al modo usuario
        
    def returnToPcbTable(self):
        self.shortScheduler.retryAdd(self.cpu.pcbCurrent)

    def isModeKernel(self):
        return self.modeKernel
    
    def runProcess(self, aProgramName):
        self.manageIRQ.newInterrupt(aProgramName)
        
    def insertProcess(self, aProgramName):
        newPCB = PCB(aProgramName)
        self.longScheduler.handle(newPCB)
        
    def addDevice(self, aDevice):
        self.handlerIO.addDevice(aDevice)
        