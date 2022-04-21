from typing import List, Dict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_: Dict[int, int] = {}

        for num in nums:
            if num not in dict_:
                dict_[num] = 1
            else:
                dict_[num] += 1

        for k, v in dict_.items():
            if v == 1:
                return k


if __name__ == "__main__":
    print(Solution().singleNumber([4, 1, 2, 1, 2]))
