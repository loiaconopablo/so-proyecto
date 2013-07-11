'''
Created on 10/07/2013

@author: Pablo Loiacono
'''
import unittest
from Disk import *
from Program import *

class TestDisk(unittest.TestCase):

    def setUp(self):
        self.disk = Disk()
        self.progrA = Program("Program1")
        self.progrB = Program("Program2")

    def tearDown(self):
        pass
    
    def testBuilder(self):
        self.assertEquals(len(self.disk.listOfProgram),0)
        
    def testLoadAndIsInDisk(self):
        self.disk.load(self.progrA)
        self.disk.load(self.progrB) 
        self.assertEquals(self.disk.listOfProgram["Program1"], self.progrA)
        self.assertTrue("Program2" in self.disk.listOfProgram.keys() )
        self.assertTrue(self.disk.isInDisk("Program2"))
        self.assertTrue(self.disk.isInDisk("Program1"))
        self.assertFalse(self.disk.isInDisk("Program3"))
        
    def testGet(self):
        self.disk.load(self.progrA)
        self.disk.load(self.progrB) 
        self.assertEquals(self.disk.get("Program1"), self.progrA)
        self.assertEquals(self.disk.get("Program2"), self.progrB)
        


suite = unittest.TestLoader().loadTestsFromTestCase(TestDisk)
unittest.TextTestRunner(verbosity=2).run(suite)