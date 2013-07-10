'''
@author: Pablo
'''
from Timer import *
from State import *

class CPU:

    def __init__(self, aKernel):
        self.kernel = aKernel
        self.pc = 0
        self.pcbCurrent = None
        self.timer = Timer()
        
    def initializeThread(self):
        self.timer.initializeThread()
        
    def fetchInstruction(self,): #lo hace en modo usuario VERIFICAR
        if self.hayPCB():
            if self.pcbCurrent.isProgramInMemory():
                self.runInstruccion()              
            else:
                self.kernel.mmu.saveInMemory(self.pcbCurrent)#carga el programa en memoria
                self.runInstruccion()
            self.isLastInstruccion()
            
    def hayPCB(self):
        return self.pcbCurrent != None          


    def runInstruccion(self):
        nextInstruccion = self.readInstruccion()
        if self.nextIsIO(nextInstruccion): # Validar (si es una instruccion de I/O) para hacer una IRQ
            self.iOInterrupt(self.pcbCurrent, nextInstruccion) #EL PC LO INCREMENTA LUEGO DE EL HANDLER IO EJECUTE LA INSTRUCCION
        else:
            self.runCPUInstrucction(nextInstruccion)

    def runCPUInstrucction(self, nextInstruccion):
        self.pcbCurrent.changeStatus(State.RUNNING)
        nextInstruccion.execute()
        self.pcbCurrent.increasePc()
        self.pcbCurrent.changeStatus(State.READY) #Analizar si es necesario
    
    def readInstruccion(self):
        instruccion=self.kernel.mmu.read(self.pcbCurrent.nextDirInstruccion())
        return instruccion

    def nextIsIO(self, instruccion):
        return instruccion.isIO()

    def isLastInstruccion(self):
        if  self.pcbCurrent.isLastInstruccion():
            self.killInterrupt(self.pcbCurrent)
                   
    def iOInterrupt(self, aPCB , nextInstruccion):
        self.kernel.manageIRQ.iOInterrupt(aPCB, nextInstruccion)

    def killInterrupt(self, aPCB):
        self.kernel.manageIRQ.killInterrupt(aPCB)
    
    def setPCB(self , aPCB):
        self.pcbCurrent = aPCB
        
    def getPCB(self):
        return self.pcbCurrent()
