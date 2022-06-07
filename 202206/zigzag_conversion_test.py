import unittest
from zigzag_conversion import Solution


class ConvertTest(unittest.TestCase):
    def test1(self):
        t = Solution().convert("PAYPALISHIRING", 3)
        self.assertEqual(t, "PAHNAPLSIIGYIR")
    
    def test2(self):
        t = Solution().convert("PAYPALISHIRING", 4)
        self.assertEqual(t, "PINALSIGYAHRPI")

    def test3(self):
        t = Solution().convert("A", 1)
        self.assertEqual(t, "A")
        

if __name__=="__main__":
    unittest.main()