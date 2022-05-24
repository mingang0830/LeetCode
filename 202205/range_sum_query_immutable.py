from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        """
        self.nums = nums
        """

        # prefix sum 알고리즘
        self.presum = [0]
        for i in range(len(nums)):
            self.presum.append(self.presum[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        """
        result = 0
        for num in self.nums[left:right+1]:
            result+= num
        return result
        """

        return self.presum[right + 1] - self.presum[left]
        


