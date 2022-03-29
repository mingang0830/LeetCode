from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Time Limit Exceeded

        result: List[int]= []
        for idx in range(len(nums)):
            div: int = idx + 1
            while div <= len(nums):
                temp: List[int] = nums[idx:div]
                result.append(sum(temp))
                div += 1
        return max(result)
        """
        current_subarray: int = nums[0]
        max_subarray: int = current_subarray

        for num in nums[1:]:

            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray





