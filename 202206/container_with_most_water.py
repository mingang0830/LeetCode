from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Time Limit Exceeded

        max_area = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                max_area = max(max_area,min(height[i],height[j])*(j-i))
        return max_area
        """

        