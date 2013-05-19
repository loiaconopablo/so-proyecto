'''
@author: Pablo
'''

class CPU:

    def __init__(self,sched,kernel,cola,memory,clock):
        self.scheduler = sched
        self.kernel = kernel
        self.cola = cola#QReady
        self.mmu = memory
        self.clock = clock
