import unittest
from valid_perfect_square import Solution


class PerfectSquareTest(unittest.TestCase):
    def test1(self):
        t = Solution().isPerfectSquare(16)
        self.assertEqual(t, True)

    def test2(self):
        t = Solution().isPerfectSquare(14)
        self.assertEqual(t, False)

    def test3(self):
        t = Solution().isPerfectSquare(1)
        self.assertEqual(t, True)

    def test4(self):
        t = Solution().isPerfectSquare(2000105819)
        self.assertEqual(t, False)


if __name__=="__main__":
    unittest.main()