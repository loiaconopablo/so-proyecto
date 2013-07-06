'''
Created on 06/07/2013

@author: Pablo Loiacono
'''
import unittest

from Disk import *
from Program import *

class TestDisk(unittest.TestCase):


    def setUp(self):
        self.disk=Disk()
        self.progrA = Program("Program1")
        self.progrB = Program("Program5")


    def tearDown(self):
        pass
    
    def testIsInDisk(self):
        self.disk.load(self.progrA)
        self.assertTrue(self.disk.isInDisk("Program1"))
        self.assertFalse(self.disk.isInDisk("Program2"))
        
    def testLoad(self):
        self.disk.load(self.progrA)
        self.disk.load(self.progrB)
        self.assertEquals(2, len(self.disk.listOfProgram))
        self.assertTrue(self.disk.isInDisk("Program5"))
        self.assertTrue(self.disk.isInDisk("Program1"))
    
    def testGet(self):
        self.disk.load(self.progrA)
        self.assertEquals(self.progrA, self.disk.get('Program1'))
        self.assertNotEquals(self.progrB, self.disk.get('Program1'))

suite = unittest.TestLoader().loadTestsFromTestCase(TestDisk)
unittest.TextTestRunner(verbosity=2).run(suite)