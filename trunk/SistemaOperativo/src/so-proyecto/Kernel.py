class Kernel:

    def __init__(self,cpu,policity,aClock,aMemory):

        self.processor = cpu
        self.modeKernel = False #comienza en modo usuario
        self.pcb = None # pcbActual
        self.scheduler = Scheduler(policity)
        self.clock = aClock
        self.memory = aMemory


