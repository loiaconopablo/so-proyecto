#Testeando el PyDev y commit!!!
'''
Created on 18/05/2013

@author: Pablo
'''
from Kernel import *

class Timer:
    def __init__(self, aKernel):
        self.quantum = kernel.scheduler.quamtum()
        self.currentQuantum = self.quantum
        self.clock = Clock()
        self.kernel= aKernel

    def decreasedQuamtum(self):
        self.currentQuantum= self.currentQuantum - 1
        return self.currentQuantum
              
    def reset(self):
        self.currentQuantum = self.quantum
    
    def timeOut(self):
        return self.currentQuantum == 0
    
    def timeOutInterrupt(self, aPCB):
        self.kernel.manageIRQ.timeOutInterrupt(aPCB)
        
    def run(self):
        if not self.kernel.isModeKernel():
            self.decreasedQuamtum()
            if self.timeOut():
                self.timeOutInterrupt()
            else: self.kernel.cpu.fetchInstruction()