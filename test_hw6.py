'''
Created on Mar 1, 2015
Last modified on Mar 4, 2016

@author: Brian Borowski

CS115 - Hw 6 Test Script
'''
import unittest
import hw6

class Test(unittest.TestCase):

    def test01(self):
        sequence = '0' * 64
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '1111100000111110000000010')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 0.390625, 4)

    def test02(self):
        sequence = '01' * 32
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '00001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 5.0, 4)

    def test03(self):
        sequence = '10' * 32
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '0000000001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 5.078125, 4)

    def test04(self):
        sequence = '0' * hw6.MAX_RUN_LENGTH + '1' * hw6.MAX_RUN_LENGTH + '0' * (64 - 2 * hw6.MAX_RUN_LENGTH)
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '111111111100010')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 0.234375, 4)

    def test05(self):
        sequence = '0' * (hw6.MAX_RUN_LENGTH + 1) + '1' * (hw6.MAX_RUN_LENGTH + 1) + '0' * (64 - 2 * hw6.MAX_RUN_LENGTH - 2)
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '111110000000001111110000000001')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 0.46875, 4)

    def test06(self):
        sequence = '1' * hw6.MAX_RUN_LENGTH + '0' * hw6.MAX_RUN_LENGTH + '1' * (64 - 2 * hw6.MAX_RUN_LENGTH)
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '00000111111111100010')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 0.3125, 4)
        
    def test07(self):
        sequence = "0"*9 + "01100110"*3 + "0"*9 + "00001000" + "01000010" + "01111110" + "0"*9
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '010100001000010000100001000010000100001000010000100001000010011100000100100000010010000001000100011001010')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 1.4, 4)
    
    def test08(self):
        sequence = "1"*10 + "0"*8 + "10000000"*3 + "1"*8 + "0" + "00000001"*3 + "1"*8 + "0"
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '0000001010010000000100111000010011100001001110100001000000010011100001001110100100001')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 1.0119047619047619, 4)

if __name__ == "__main__":
    unittest.main()
