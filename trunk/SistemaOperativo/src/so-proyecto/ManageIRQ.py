'''
Created on 20/05/2013

@author: Pablo
'''
from Kernel import *

class ManageIRQ:
    def __init__(self, aKernel, aHandler):
            self.kernel = aKernel
        
    def iOInterrupt(self, pcb , nextInstruccion):
        self.kernel.modoOn()
        self.kernel.handlerIO.handle(pcb, nextInstruccion)
        print("Se mando un proceso a la cola de I/O")
        self.kernel.cpu.setPCB(None)
        self.kernel.contextSwitch()
        self.kernel.modoOff()

    def killInterrupt(self, pcb):
        self.kernel.modoOn()
        self.kernel.pcbFinish.append(self.kernel.cpu.getPCB())  # se guarda el pcb finalizado en la lista.
        self.kernel.cpu.pcb = null  # borrar el pcb terminado
        print("Finalizo el proceso actual")
        self.kernel.contextSwitch()
        self.kernel.modoOff()
        
    def timeOutInterrupt(self):
        self.kernel.modoOn()
        self.kernel.contextSwitch()
        print("Se termino el tiempo de ejecuciòn del proceso actual")
        self.kernel.modoOff()
        
    def nilInterrupt(self):  # Terminar de hacer
        self.kernel.modoOn()
        print("No hay mas programas en la QReady")
        self.handler.nilInterrupt()    
        self.kernel.modoOff()
        
    def newInterrupt(self, program):  # Terminar de hacer
        print("Entro un nuevo proceso")
        self.kernel.insertProcess(program)
        self.kernel.reschedule()    
            
        
