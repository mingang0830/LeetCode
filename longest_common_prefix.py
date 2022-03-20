from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix: str = ""
        for idx, char in enumerate(strs[0]):
            for str_ in strs:
                if idx >= len(str_) or str_[idx] != char:  # index가 len 보다 작아야 범위 내
                    return prefix
            prefix += char


