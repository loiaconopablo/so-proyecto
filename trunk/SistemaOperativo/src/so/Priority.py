'''
@author: Pablo
'''
#===============================================================================
# import threading       NO FUE NECESARIO
# semaforo = threading.Lock()  
#===============================================================================

class Priority:

    def __init__(self):
        self.qReady = []

    def next(self):
        #semaforo.acquire()
        return self.qReady.pop(0)
        #semaforo.release()
        
    def add(self, aPCB):
        #semaforo.acquire()
        self.qReady.append(aPCB)
        self.qReady.sort(key = lambda pcb:pcb.priority)
        return self.qReady
        #semaforo.release()

    def retryAdd(self, aPCB):
        aPCB.decreasePriority()
        self.add(aPCB)
    
    def isRR(self):
        return False

