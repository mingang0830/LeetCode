from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time Limit Exceeded

        temp: List[int] = []
        for num in nums:
            if num in temp:
                return True
            temp.append(num)
        
        return False
        """
        return len(set(nums)) < len(nums)
        


if __name__ == "__main__":
    print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))