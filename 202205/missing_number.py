from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num: int = max(nums)
        range_: range = range(0,max_num+1)
        difference_: List[int] = list(set(range_) - set(nums))
        
        if difference_:
            return difference_[0]
        else:
            return max_num + 1

if __name__=="__main__":
    print(Solution().missingNumber([0,1])) 