from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix: str = ""

        if "" in strs:
            return prefix

        if len(strs) == 1:
            return strs[0]

        for idx, char in enumerate(strs[0]):
            for str_ in strs:
                if idx >= len(str_) and str_[idx] != char:  # index가 len 보다 작아야 범위 내
                    return prefix
            prefix += char
        return prefix


