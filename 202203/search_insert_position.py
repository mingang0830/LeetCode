from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        i = 0
        while i < len(nums) and nums[i] < target:
            i += 1
        return i
        """

        # 이진 탐색 트리
        # left < mid < right
        left: int = 0
        right: int = len(nums) - 1
        while left <= right:
            mid: int = (left + right) // 2
            if nums[mid] > target:  # left 탐색
                right = mid - 1
            elif nums[mid] < target:  # right 탐색
                left = mid + 1
            else:  # 값이 맞을 때
                return mid

        return left  # 값이 없을 때

