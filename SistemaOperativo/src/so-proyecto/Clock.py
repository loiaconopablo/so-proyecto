'''
Created on 21/05/2013

@author: Pablo Loiacono
'''
from Timer import *

class Clock(Thread):

    def __init__(self, timer):
        Thread.__init__(self)
        self.timer = timer

    def run(self):
        while (True):
            sleep(1)
            self.timer.run()

               
        
    
