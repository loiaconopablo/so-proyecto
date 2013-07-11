'''
Created on 20/05/2013

@author: Pablo
'''
from Kernel import *
from CPU import *
from HandlerIO import *
from PCB import *

class ManageIRQ:
    def __init__(self, aKernel):
            self.kernel = aKernel
        
    def iOInterrupt(self, pcb , nextInstruccion):
        self.kernel.modeOn()
        self.kernel.handlerIO.handleIO(pcb, nextInstruccion)
        print("Se mando un proceso a la cola de I/O")
        self.kernel.cpu.setPCB(None)
        self.kernel.contextSwitch()
        self.kernel.modeOff()

    def killInterrupt(self):
        self.kernel.modeOn()
        print("Finalizo la ejecucion del "+ self.kernel.cpu.pcbCurrent.getNameProgram())
        self.kernel.pcbFinish.append(self.kernel.cpu.getPCB())  # se guarda el pcb finalizado en la lista.
        self.kernel.mmu.release(self.kernel.cpu.pcbCurrent) #LIBERA EL ESPACIO DONDE ESTABA ASIGNADO EL PCB.
        self.kernel.longScheduler.checkForSpace()#Si hay pcb en la lista de espera
        self.kernel.cpu.setPCB(None)  # borrar el pcb terminado
        self.kernel.modeOff()
        
    def timeOutInterrupt(self):
        self.kernel.modeOn()
        print("Se termino el tiempo de ejecucion del "+ self.kernel.cpu.pcbCurrent.getNameProgram())
        self.kernel.contextSwitch()
        self.kernel.modeOff()
        
    def nilInterrupt(self):
        self.kernel.modeOn()
        if self.kernel.shortScheduler.isEmpty():
            print("No hay programas en la QReady")
            self.kernel.cpu.timer.reset()
        else: self.kernel.contextSwitch()
        self.kernel.modeOff()
        
    def newInterrupt(self, aProgramName):  
        self.kernel.insertProcess(aProgramName)  
        print("Entro un nuevo proceso")

    def endIO(self, pcb):
        print("Se agrega el proceso que termino IO a la cola de ready")
        pcb.increasePc()
        self.kernel.shortScheduler.retryAdd(pcb)
        
    def noFoundProgram(self, aNameOfProgram):
        self.kernel.modeOn()
        print("El programa " + aNameOfProgram + " no se encuentra cargado en disco.Carguelo y vuela a ejecutar el programa")
        self.kernel.modeOff()
