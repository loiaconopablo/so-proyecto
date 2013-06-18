'''
@author: Pablo
'''
from Instruccion import *
from IOInstruccion import *
from Kernel import *

class CPU:

    def __init__(self, kernel):
        self.kernel = kernel
        self.mmu = memory
        self.pc = 0
        self.pcbCurrent = None
        self.timer = Timer()


    def fetchInstruction(self,):
        if self.hayPCB():
            if self.pcbCurrent.isInMemory():
                self.runInstruccion()              
            else:
                self.mmu.saveInMemory(self.pcbCurrent)#carga el programa en memoria
                self.runInstruccion()
            self.isLastInstruccion()
              #  if (preguntar si es la ultima instruccion)): Armar condicion bien
              #     self.killInterrupt(self.pcbCurrent)

    def runInstruccion(self):
        nextInstruccion = self.readInstruccion()
        if self.nextIsIO(nextInstruccion): # Validar (si es una instruccion de I/O) para hacer una IRQ
            self.iOInterrupt(self.pcbCurrent, nextInstruccion)
            #EL PC LO INCREMENTA LUEGO DE EL HANDLER IO EJECUTE LA INSTRUCCION
        else:
            nextInstruccion.execute()
            self.pcbCurrent.increasePc()
    
    def hayPCB(self):
        return self.pcbCurrent != None
                   
    def iOInterrupt(self, aPCB , nextInstruccion):
        self.kernel.manageIRQ.iOInterrupt(aPCB, nextInstruccion)
        
    def readInstruccion(self):
        instruccion=self.memory.read(self.nextDirInstruccion())
        return instruccion.isIO()

    def nextIsIO(self, instruccion):
        return instruccion.isIO()

    def killInterrupt(self, aPCB):
        self.kernel.manageIRQ.killInterrupt(aPCB)
    
    def setPCB(self , aPCB):
        self.pcbCurrent = aPCB
        
    def getPCB(self):
        return self.pcbCurrent
