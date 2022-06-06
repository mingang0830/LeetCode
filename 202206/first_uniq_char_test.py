import unittest
from first_uniq_char import Solution


class FirstUniqCharTest(unittest.TestCase):
    def test1(self):
        t = Solution().firstUniqChar("leetcode")
        self.assertEqual(t, 0)
    
    def test2(self):
        t = Solution().firstUniqChar("loveleetcode")
        self.assertEqual(t, 2)

    def test3(self):
        t = Solution().firstUniqChar("aabb")
        self.assertEqual(t, -1)
        

if __name__=="__main__":
    unittest.main()