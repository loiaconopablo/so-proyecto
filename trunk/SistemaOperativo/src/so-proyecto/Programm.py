class Programm:
 def __init__(self,aMemory):
                self.instrucciones = []
                self.memory = aMemory
        
        def add(self, aObject):
                self.instrucciones.append(aObject)

        def run(self):
                for i in self.instrucciones:
                        i.execute(self.memory)
