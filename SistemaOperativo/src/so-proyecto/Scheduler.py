import Queue

class Scheduler:

    def __init__(self, aPolicity):
        self.qReady = [] # lo deje como una lista
        self.policity = aPolicity
        
    def next(self):
        return self.policity.next(self.qReady)

    def add(self, aPCB):
        aPCB.changeStatus('Ready')
        self.policity.add(self.qReady, aPCB)

    def isEmpty(self):
        return len(self.qReady) == 0
