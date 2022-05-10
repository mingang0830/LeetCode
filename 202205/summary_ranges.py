from typing import List

class Solution(object):
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result: List[str] = []
        start, len_ = 0, len(nums)
        for i in range(len_):
            if i + 1 <  len_ and nums[i + 1] == nums[i] + 1:
                continue
            
            if i == start:
                result.append(str(nums[start]))
            else:
                result.append("{}->{}".format(nums[start], nums[i]))
            start = i + 1
        return result


if __name__ == "__main__":
    print(Solution().summaryRanges([0,1,2,4,5,7]))