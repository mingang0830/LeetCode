class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1
        """
        for ch in dict.fromkeys(s):
            if s.count(ch) == 1:
                return s.index(ch)
        return -1