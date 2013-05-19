'''
Created on 18/05/2013

@author: Pablo
'''
from Kernel import *

class Timer:
    def __init__(self, kernel):
        if kernel.scheduler.whitRR(): 
            self.quantum = kernel.scheduler.quamtum()
        else: self.quantum = 15
        self.currentQuantum = self.quantum

    def decreased(self):
        self.currentQuantum-= 1
        return self.currentQuantum
              
    def reset(self):
        self.currentQuantum = self.quantum