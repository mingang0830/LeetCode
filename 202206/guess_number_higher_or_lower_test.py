import unittest
from guess_number_higher_or_lower import Solution


class GuessNumberTest(unittest.TestCase):
    def test1(self):
        t = Solution().guessNumber(10, 6)
        self.assertEqual(t, 6)
    
    def test2(self):
        t = Solution().guessNumber(1, 1)
        self.assertEqual(t, 1)

    def test3(self):
        t = Solution().guessNumber(2, 1)
        self.assertEqual(t, 1)
    

if __name__=="__main__":
    unittest.main()