'''
Created on 20/05/2013

@author: Pablo
'''
from Kernel import *

class ManageIRQ:
    def __init__(self, aKernel):
            self.kernel= aKernel
        
    def iOInterrupt(self, pcb):
        self.kernel.modoOff()
        print("Se mando un proceso a la cola de I/O")
        self.kernel.handlerIO.handle(pcb)
        self.kernel.modoOn()

    def killInterrupt(self, pcb):
        self.kernel.modoOff()
        self.kernel.cpu.pcb=null # borrar el pcb terminado, ver si lo guardamos en alguna lista
        print("Finalizo el proceso actual")
        self.kernel.contextSwitch()
        self.kernel.modoOn()
        
    def timeOutInterrupt(self):
        self.kernel.modoOff()
        print("Se termino el tiempo de ejecuciòn del proceso actual")
        self.handler.timeOutInterrupt()
        self.kernel.modoOn()
        
    def nilInterrupt(self):
        self.kernel.modoOff()
        print("No hay mas programas en la QReady")
        self.handler.nilInterrupt()    
        self.kernel.modoOn()
        
    def newInterrupt(self,process):
        print("Entro un nuevo proceso")
        self.kernel.insertProcess(process)
        self.kernel.reschedule()    
            
        