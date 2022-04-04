from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        n1_idx = m - 1
        n2_idx = n - 1
        total_idx = m + n - 1
        while n1_idx >= 0 and n2_idx >= 0:
            if nums1[n1_idx] >= nums2[n2_idx]:
                nums1[total_idx] = nums1[n1_idx]
                n1_idx -= 1
            elif nums1[n1_idx] < nums2[n2_idx]:
                nums1[total_idx] = nums2[n2_idx]
                n2_idx -= 1
            total_idx -= 1

        if n2_idx >= 0:  # n1_idx 는 음수
            nums1[:total_idx + 1] = nums2[:n2_idx + 1]
