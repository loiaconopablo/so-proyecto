'''
@author: Pablo
'''

class RoundRobin:

    def __init__(self, aQuantum):
        self.quantum = aQuantum  
        self.qReady = []

    def next(self):
        return self.qReady.pop(0)

    def add(self,aPCB):
        self.qReady.append(aPCB)
        return self.qReady
    
    def isRR(self):
        return True 