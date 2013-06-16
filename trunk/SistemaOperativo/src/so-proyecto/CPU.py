'''
@author: Pablo
'''

class CPU:

    def __init__(self, kernel):
        self.kernel = kernel
        self.mmu = memory
        self.pc = 0
        self.pcbCurrent = None
        self.timer = Timer()

    def fetchInstruction(self,):
        if self.hayPCB():
            if self.pcbCurrent.isInMemory():
                if self.nextIsIO():  # Validar (si es una instruccion de I/O) para hacer una IRQ
                    self.iOInterrupt(self.pcbCurrent)
                else:
                    self.pcbCurrent.runInstruccion()
                    self.pcbCurrent
            else:
                self.mmu.saveInMemory(self.pcbCurrent)#carga el programa en memoria
            
            
            self.instruccion.run()
            self.pcbCurrent.increasePc()
              #  if (preguntar si es la ultima instruccion)): Armar condicion bien
              #     self.killInterrupt(self.pcbCurrent)
    def hayPCB(self):
        return self.pcbCurrent != None

    def nextIsIO(self):
        return self.pcbCurrent.nextIsIO()
                   
    def iOInterrupt(self, aPCB):
        self.kernel.manageIRQ.iOInterrupt(aPCB)

    def killInterrupt(self, aPCB):
        self.kernel.manageIRQ.killInterrupt(aPCB)
    
    def setPCB(self , aPCB):
        self.pcbCurrent = aPCB
        
    def getPCB(self):
        return self.pcbCurrent
