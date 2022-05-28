from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> List[str]:
        """
        for i in range(len(s)):
            s.insert(0,s.pop(i))
        return s
        """
        for i in range(len(s)//2):
            s[i], s[-(i+1)] = s[-(i+1)], s[i] 
        return s
