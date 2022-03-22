from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        for i in nums:
            if i == val:
                nums.remove(i)
        return len(nums)

        for문의 num이 수정되기 때문에 실패
        temp = num[:] 만들어서 해봤는데 내가 돌렸을땐 문제가 없는데 leetcode에서는 실패로 뜬다 왜지..
        """
        while val in nums:
            nums.remove(val)
        return len(nums)

