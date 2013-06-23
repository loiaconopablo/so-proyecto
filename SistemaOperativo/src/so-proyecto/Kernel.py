'''
@author: Pablo
'''

from Scheduler.py import *
from CPU import *
from ManageIRQ import *

class Kernel:

    def __init__(self, policity, aMemory):

        self.cpu = CPU(self, aMemory )
        self.modeKernel = False  # comienza en modo usuario
        self.scheduler = Scheduler(policity, self)
        self.longScheduler = LongScheduler(scheduler)#revisar
        self.pcbCurrent = None
        self.handlerIO = HandlerIO()
        self.memory = aMemory
        self.timer = Timer(self) 
        self.pcbFinish = []
        self.manageIRQ = ManageIRQ(self)
        
    # def run(self):

    def modeOn(self):  # lo pone en modo kernel
        self.modeKernel = True  

    def modeOff(self):  # lo pone en modo usuario
        self.modeKernel = False
        
    def setNextPcb(self):
        self.cpu.setPCB(self.scheduler.next())


    def contextSwitch(self):
        self.modeOn() # coloco en modo kernel
        if self.cpu.pcbCurrent == None:  # #chequeo si el CPU finalizo el ultimo PCB o lo 
            self.setNextPcb()            # #  seteo en el pcb del CPU el proximo pcb
        else:
            self.returnToPcbTable()  # # vuelvo a poner el pcb en la cola qReady
            self.setNextPcb()  # #  seteo en el pcb del CPU el proximo pcb
        self.modoOff() #vuelvo al modo usuario
        
    def returnToPcbTable(self):
        self.scheduler.retryAdd(self.cpu.pcbCurrent)

    def isModeKernel(self):
        return self.modeKernel
    
    def addProcess(self, aProgramName):
        self.manageIRQ.newInterrupt(aProgramName)
        
    def insertProcess(self, aProgramName):
        self #Continuar

        