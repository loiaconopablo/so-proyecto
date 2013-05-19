'''
@author: Pablo
'''


class Fifo:

    def __init__(self):
        self.qReady = []

    def next(self):
        return self.qReady.pop(0)

    def add(self,qReady,aPCB):
        return self.qReady.append(aPCB)

    def isRR(self):
        return False