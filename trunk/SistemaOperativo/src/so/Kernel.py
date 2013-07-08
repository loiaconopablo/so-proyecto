'''
@author: Pablo
'''

from Scheduler import *
from CPU import *
from ManageIRQ import *
from Program import *
from PCB import *
from Timer import *
from Disk import *


class Kernel:

    def __init__(self, policity, aMMU):
        self.cpu = CPU(self)
        self.modeKernel = False  # comienza en modo usuario
        self.shortScheduler = ShortScheduler(policity, self)
        self.longScheduler = LongScheduler(policity, self)#revisar
        self.pcbCurrent = None
        self.mmu = aMMU #Realizar
        self.timer = Timer(self) 
        self.pcbFinish = []
        self.manageIRQ = ManageIRQ(self)
        self.disk = Disk()
        self.handlerIO = HandlerIO(self.manageIRQ)
        
    # def run(self):
    def initializeThread(self):
        self # Inicializar todos los threads
    
    def downThread(self):
        self #ver como bajar todos los threasd
            
    def modeOn(self):  # lo pone en modo kernel
        self.modeKernel = True  

    def modeOff(self):  # lo pone en modo usuario
        self.modeKernel = False
        
    def setNextPcb(self):
        self.cpu.setPCB(self.shortScheduler.next())
        self.timer.currentQuantum.reset()

    def contextSwitch(self):
        self.modeOn() # coloco en modo kernel
        if self.cpu.pcbCurrent == None:  # #chequeo si el CPU finalizo el ultimo PCB o lo 
            self.setNextPcb()            # #  seteo en el pcb del CPU el proximo pcb
        else:
            self.returnToPcbTable()  # # vuelvo a poner el pcb en la cola qReady
            self.setNextPcb()  # #  seteo en el pcb del CPU el proximo pcb
        self.modoOff() #vuelvo al modo usuario
        
    def returnToPcbTable(self):
        self.shortScheduler.retryAdd(self.cpu.pcbCurrent)

    def isModeKernel(self):
        return self.modeKernel
    
    def addProcess(self, aProgramName):
        self.manageIRQ.newInterrupt(aProgramName)
        
    def insertProcess(self, aProgramName):
        self.PCB = self.PCB(aProgramName)
        self.longScheduler.handle(self.PCB)
        