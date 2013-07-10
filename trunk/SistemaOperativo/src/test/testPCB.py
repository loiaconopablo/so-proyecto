'''
Created on 10/07/2013

@author: Pablo Loiacono
'''
import unittest
from PCB import *
from State import *

class TestPCB(unittest.TestCase):


    def setUp(self):
        self.OnePCB = PCB("Program1")
        self.TwoPCB = PCB("Program2",20)

    def tearDown(self):
        pass

    def testBuilder(self):
        self.assertEquals(self.OnePCB.pc,0)
        self.assertEquals(self.OnePCB.priority,10)
        self.assertEquals(self.TwoPCB.priority,20)
        self.assertTrue(self.TwoPCB.dirBase==None)
        self.assertEquals(self.OnePCB.status,State.NEW)

    def testIncreasePc(self):
        self.OnePCB.increasePc()
        self.assertTrue(self.OnePCB.pc==1)
        self.TwoPCB.increasePc()
        self.TwoPCB.increasePc()
        self.TwoPCB.increasePc()
        self.assertTrue(self.TwoPCB.pc==3)
        
    def testsetDirBase(self):
        self.OnePCB.setDirBase(10)
        self.assertTrue(self.OnePCB.dirBase!=None)
        self.assertTrue(self.OnePCB.dirBase==10)
        
    def testNextDirInstruccion(self):
        self.OnePCB.setDirBase(10)
        self.assertEquals(self.OnePCB.nextDirInstruccion(),10)
        self.OnePCB.increasePc()
        self.assertEquals(self.OnePCB.nextDirInstruccion(),11)
    
    def testDecreasePriority(self):
        self.OnePCB.decreasePriority()
        self.assertEquals(self.OnePCB.priority,9)
        self.OnePCB.decreasePriority()
        self.OnePCB.decreasePriority()
        self.OnePCB.decreasePriority()
        self.assertEquals(self.OnePCB.priority,6)
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestPCB)
unittest.TextTestRunner(verbosity=2).run(suite)
