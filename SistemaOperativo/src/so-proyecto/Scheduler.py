'''
@author: Pablo
'''

class Scheduler:

    def __init__(self, aPolicity):
       #la implemente en cada politica=  self.qReady = []
        self.policity = aPolicity
        
    def next(self):
        return self.policity.next()

    def add(self, aPCB):
        aPCB.changeStatus(State.READY)
        self.policity.add(aPCB)
        
    def retryAdd(self, aPCB):
        aPCB.changeStatus(State.READY)
        self.policity.retryAdd(aPCB)

    def isEmpty(self):
        return len(self.policity.qReady) == 0
    
    def quamtum(self):
        if self.policity.isRR():
            return self.policity.quantum
        else: return 10
        
    

