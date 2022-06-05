import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #{"a":1, "b":1...}
        ransom_dict = collections.Counter(ransomNote) 
        magazine_dict = collections.Counter(magazine)

        for c in ransom_dict:
            if c not in magazine_dict:
                return False
            elif ransom_dict[c] > magazine_dict[c]:
                return False
        return True