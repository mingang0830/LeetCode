import unittest
import power_of_three


class PowerOfTreeTest(unittest.TestCase):

    def test1(self):
        t = power_of_three.Solution().isPowerOfThree(27)
        self.assertEqual(t, True)
    
    def test2(self):
        t = power_of_three.Solution().isPowerOfThree(0)
        self.assertEqual(t, False)
    
    def test3(self):
        t = power_of_three.Solution().isPowerOfThree(9)
        self.assertEqual(t, True)


if __name__=="__main__":
    unittest.main()