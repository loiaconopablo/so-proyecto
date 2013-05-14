class Priority:

    def __init__(self):
       self

    def next(self, qReady):
        lenght=len(qReady)
        return qReady.pop(lenght-1)

    def add(qReadyself, qReady, aPCB):
       qReady.append(aPCB)
       qReady.sorted(self.queue, key = lambda pcb:pcb.priority)
      
