import unittest
import nim_game


class NimGameTest(unittest.TestCase):
    def test1(self):
        t = nim_game.Solution().canWinNim(4)
        self.assertAlmostEqual(t,False)
    
    def test2(self):
        t = nim_game.Solution().canWinNim(1)
        self.assertAlmostEqual(t,True)

    def test3(self):
        t = nim_game.Solution().canWinNim(2)
        self.assertAlmostEqual(t,True)
    
    def test4(self):
        t = nim_game.Solution().canWinNim(8)
        self.assertAlmostEqual(t,False)

if __name__ =="__main__":
    unittest.main()