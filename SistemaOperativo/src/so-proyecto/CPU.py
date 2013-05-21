'''
@author: Pablo
'''

class CPU:

    def __init__(self,kernel):
        self.kernel = kernel
        self.mmu = memory
        self.pc=0
        self.pcbCurrent = null
        self.timer = Timer()
        
    def fetchInstruction(self,):
        if self.pcbCurrent != null:
            self.instruction = self.mmu.get(self.pcbCurrent.PC)
            self.instruccion.run() # esta linea la copie de lo de Marcelo del pizarron, preguntar que es lo que hace el run de la instrucciom
                                  # a diferencia del execute()
            self.pcbCurrent.increasePc()
            if self.instruction.isIO():#Validar (si es una instruccion de I/O) para hacer una IRQ
                self.iOInterrupt(self.pcbCurrent)
            else:            
                self.instruction.execute()
              #  if (preguntar si es la ultima instruccion)): Armar condicion bien
              #     self.killInterrupt(self.pcbCurrent)
                    
            
    def iOInterrupt(self, aPCB):
        self.kernel.manageIRQ.iOInterrupt(aPCB)

    def killInterrupt(self, aPCB):
        self.kernel.manageIRQ.killInterrupt(aPCB)
    
    def setPCB(self , aPCB):
        self.pcbCurrent= aPCB
        