
class Fifo:

    def __init__(self):
        self

    def next(self, qReady):
        return qReady.pop(0)

    def add(self,qReady,aPCB):
        return qReady.append(aPCB)
