from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        for i in nums:
            while nums.count(i) != 1:
                nums.remove(i)
        return len(nums)
        """

        #  시간 복잡도 줄이기 O(n)
        if len(nums) == 0:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1  # count & pointer
                # sorted in non-decreasing order 이기 때문에 다음 pointer를 직전에 비교한 값으로 변경해주면 중복 카운팅X
                nums[i] = nums[j]

        return i + 1



