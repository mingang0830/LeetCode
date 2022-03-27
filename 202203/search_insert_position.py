from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 이진 탐색 트리
        # left < mid < right
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:  # left 탐색
                right = mid - 1
            elif nums[mid] < target:  # right 탐색
                left = mid + 1
            else:  # 값이 맞을 때
                return mid

        return left  # 값이 없을 때



print(Solution().searchInsert([1,3,6,7,8], 2))