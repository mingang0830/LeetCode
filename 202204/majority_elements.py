from typing import List, Dict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Time Limit Exceeded

        return max(nums, key=nums.count)
        """
        dict_: Dict[int, int] = {}
        for num in nums:
            if num not in dict_:
                dict_[num] = 1
            else:
                dict_[num] += 1
            
            # The majority element is the element that appears more than ⌊n / 2⌋ times.
            if dict_[num] > len(nums)/2:
                return num

        # return max(dict_, key=dict_.get) max value에 대한 key

             


if __name__ == "__main__":
    print(Solution().majorityElement([2,2,1,1,1,2,2]))