'''
Created on 18/05/2013

@author: Pablo
'''
from Clock import *

class Timer:
    def __init__(self, aKernel):
        self.quantum = aKernel.shortScheduler.quamtum()
        self.currentQuantum = self.quantum
        self.clock = Clock(self)
        self.kernel = aKernel
    
    def initializeThread(self):
        self.clock.start()

    def decreasedQuamtum(self):
        self.currentQuantum = self.currentQuantum - 1
        return self.currentQuantum
              
    def reset(self):
        self.currentQuantum = self.quantum
    
    def timeOut(self):
        return (self.currentQuantum == 0)
    
    def timeOutInterrupt(self):
        self.kernel.manageIRQ.timeOutInterrupt()
        
    def run(self):
        if not self.kernel.isModeKernel():
            if self.timeOut():
                self.timeOutInterrupt()
            else: 
                self.decreasedQuamtum()
                self.kernel.cpu.fetchInstruction()
