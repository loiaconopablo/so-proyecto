import threading
semaforo = threading.Semaphore()

class Priority:

    def __init__(self):
        self.qReady = []

    def next(self):
        #semaforo.acquire()
        lenght=len(self.qReady)
        return self.qReady.pop(lenght-1) ##ANALIZAR SI NECESITAMOS DEVOLVER EL ULTIMO O EL PRIMERO, DEPENDE COMO SE ORDENE
        #semaforo.release()
        
    def add(self, aPCB):
        #semaforo.acquire()
        self.qReady.append(aPCB)
        self.qReady.sorted(self.queue, key = lambda pcb:pcb.priority)
        return self.qReady
        #semaforo.release()

    def retryAdd(self, aPCB):
        aPCB.decreasePriority()
        self.add(aPCB)
    
    def isRR(self):
        return False

