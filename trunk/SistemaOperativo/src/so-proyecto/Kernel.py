'''
@author: Pablo
'''

class Kernel:

    def __init__(self,cpu,policity,aMemory):

        self.processor = cpu
        self.modeKernel = False #comienza en modo usuario
        self.scheduler = Scheduler(policity, quamtum=5)
        self.handlerIO = HandlerIO()
        self.memory = aMemory
        self.timer = Timer(self) 
        
    #def run(self):

    def modeOn(self):#lo pone en modo usuario
        self.modeKernel = False

    def modeOff(self):#lo pone en modo kernel
        self.modeKernel = True
        
    def next