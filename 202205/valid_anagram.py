from collections import Counter
from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        collections 모듈의 Counter 사용 - dictionary 형태로 문자열 카운팅 해줌

        return Counter(s) == Counter(t)
        """

        check_anagram: List[str] = [i for i in s]
        for j in t:
            if j in check_anagram:
                check_anagram.remove(j)
            else:
                return False
            
        return len(check_anagram) == 0


if __name__ == "__main__":
    print(Solution().isAnagram("anagram", "nagaram"))