class Priority:

    def __init__(self):
       self.qReady = []

    def next(self):
        lenght=len(self.qReady)
        self.qReady.pop(lenght-1)
        return self.qReady 

    def add(self, aPCB):
       self.qReady.append(aPCB)
       self.qReady.sorted(self.queue, key = lambda pcb:pcb.priority)
       return self.qReady

    def retryAdd(self, aPCB):
       aPCB.decreasePriority()
       self.add(aPCB)
   
    def isRR(self):
        return False
