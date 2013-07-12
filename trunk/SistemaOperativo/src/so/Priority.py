'''
@author: Pablo
'''
class Priority:

    def __init__(self):
        self.qReady = []

    def next(self):
        return self.qReady.pop(0)
        
    def add(self, aPCB):
        self.qReady.append(aPCB)
        self.qReady.sort(key = lambda pcb:pcb.priority)
        return self.qReady

    def retryAdd(self, aPCB):
        aPCB.decreasePriority()
        self.add(aPCB)
    
    def isRR(self):
        return False

