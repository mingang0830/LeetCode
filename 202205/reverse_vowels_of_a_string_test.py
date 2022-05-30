import unittest
from reverse_vowels_of_a_string import Solution


class ReverseVowelsTest(unittest.TestCase):
    def test1(self):
        t = Solution().reverseVowels("hello")
        self.assertEqual(t,"holle")
    
    def test2(self):
        t = Solution().reverseVowels("leetcode")
        self.assertEqual(t,"leotcede")
    
    def test3(self):
        t = Solution().reverseVowels("aA")
        self.assertEqual(t,"Aa")
    

if __name__=="__main__":
    unittest.main()