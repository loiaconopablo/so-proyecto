'''
@author: Pablo
'''

class CPU:

    def __init__(self, kernel):
        self.kernel = kernel
        self.mmu = memory
        self.pc = 0
        self.pcbCurrent = null
        self.timer = Timer()
        
    def fetchInstruction(self,):
        if self.pcbCurrent != null:
            self.programm = self.mmu.get(self.pcbCurrent.PC)
            self.programm.run()
            self.pcbCurrent.increasePc()
            if self.programm.isIO():  # Validar (si es una instruccion de I/O) para hacer una IRQ
                self.iOInterrupt(self.pcbCurrent)
            else:            
                self.programm.execute()
              #  if (preguntar si es la ultima instruccion)): Armar condicion bien
              #     self.killInterrupt(self.pcbCurrent)
                    
            
    def iOInterrupt(self, aPCB):
        self.kernel.manageIRQ.iOInterrupt(aPCB)

    def killInterrupt(self, aPCB):
        self.kernel.manageIRQ.killInterrupt(aPCB)
    
    def setPCB(self , aPCB):
        self.pcbCurrent = aPCB
        
