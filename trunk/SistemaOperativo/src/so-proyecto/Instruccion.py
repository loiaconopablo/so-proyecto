'''
@author: Pablo
'''


class Instruccion:
        def __init__(self, aPosition1, aPosition2, aPosition3):
                self.first = aPosition1
                self.second = aPosition2
                self.third = aPosition3
                
        def execute(self, aMemory):
                firstN = aMemory.get(self.first)
                secondN = aMemory.get(self.second)
                suma = firstN+secondN
                aMemory.put(self.third, suma)
