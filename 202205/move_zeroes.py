from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        last_non_zero_i: int = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums.insert(last_non_zero_i,nums.pop(i))
                last_non_zero_i += 1 
        return nums


