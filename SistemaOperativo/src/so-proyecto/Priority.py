class Priority:

    def __init__(self):
       self

    def next(self, qReady):
        lenght=len(qReady)
        return qReady.pop(lenght-1)

    def add(self, qReady, aPCB):
       qReady.append(aPCB)
       qReady.sorted(aPCB.priority) ## ver bien como es el metodo para ordenar.
