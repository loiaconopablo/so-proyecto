'''
Created on 21/05/2013

@author: Pablo Loiacono
'''

import time
import threading


class Clock(threading.Thread):

    def __init__(self, aTimer):
        threading.Thread.__init__(self)
        self.timer = aTimer

    def run(self):
        while (True):
            time.sleep(1)
            self.timer.run()

               
        
    
