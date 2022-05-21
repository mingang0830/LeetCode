import unittest
import move_zeroes

class MoveZeroesTest(unittest.TestCase):
    def test1(self):  
        t = move_zeroes.Solution().moveZeroes([0,1,0,3,12])
        self.assertAlmostEquals(t,[1,3,12,0,0])

    def test2(self):  
        t = move_zeroes.Solution().moveZeroes([0])
        self.assertAlmostEquals(t,[0])
        
if __name__=="__main__":
    unittest.main()