from typing import Dict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        dict_: Dict = {}
        temp: str = ""
        for c in s:
            if c in temp:
                temp = temp[temp.index(c) + 1:]
            temp += c
            dict_[temp] = len(temp)
        return max(dict_.values())


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("dvdf"))