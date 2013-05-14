class RoundRobin:

    def __init__(self, aQuantum):
        self.quantum = aQuantum  

    def next(self, qReady):
        return qReady.pop(0)

    def add(self,qReady,aPCB):
        return qReady.append(aPCB)
