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
        left=0
        right=len(height)-1
        max_area=0

        while (right-left>0) :
            max_area = max(max_area,(right-left)*min(height[left],height[right]))
                
            if height[left] >= height[right]: # 오른쪽이 낮은 경우
                right -= 1
            else: # 왼쪽이 낮은 경우
                left += 1
            
        return max_area