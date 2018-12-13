'''
Created on Feb 21, 2017

@author: BhavinSoni
'''
import unittest 
import hw4 

class Test(unittest.TestCase):  
       
    def test01(self):         
        self.assertEqual(hw4.pascal_row(0), [1])     
    
    def test02(self):         
        self.assertEqual(hw4.pascal_row(1), [1, 1])
        
    def test03(self):         
        self.assertEqual(hw4.pascal_row(3), [1, 3, 3, 1])
    
    def test04(self):         
        self.assertEqual(hw4.pascal_row(5), [1, 5, 10, 10, 5, 1])
        
    def test05(self):         
        self.assertEqual(hw4.pascal_row(9), [1, 9, 36, 84, 126, 126, 84, 36, 9, 1])
        
    def test06(self):         
        self.assertEqual(hw4.pascal_triangle(0), [[1]])
        
    def test07(self):         
        self.assertEqual(hw4.pascal_triangle(1), [[1], [1, 1]])
        
    def test08(self):         
        self.assertEqual(hw4.pascal_triangle(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
        
    def test09(self):         
        self.assertEqual(hw4.pascal_triangle(7), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]])    
        
    def test10(self):         
        self.assertEqual(hw4.pascal_triangle(11), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1], [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1], [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1]])
    
    
if __name__ == "__main__":     unittest.main()