'''
Created on 15/06/2013

@author: Pablo
'''

class DeviceManager:
    def __init__(self):
        self.devices = {}
        self.devices[Printer()] = Printer.thread  # ver bien
