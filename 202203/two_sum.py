from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, val in enumerate(nums):
            val2: int = target - val
            if val2 in nums:
                idx2: int = nums.index(val2)
                if idx != idx2:
                    return [idx, idx2]
