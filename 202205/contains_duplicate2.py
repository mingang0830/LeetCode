from typing import List, Dict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices: Dict[int, List[int]] = {}

        """
        Time Limit Exceeded

        for num in nums:      
            pos = [i for i, v in enumerate(nums) if v == num]
            if pos not in indices.values():
                    indices[num] = pos

        """
        for idx, num in enumerate(nums):      
            if num not in indices:
                    indices[num] = [idx]
            elif num in indices:
                indices[num].append(idx)

        for i in indices.values():
            if len(i) >= 2:
                for j in range(0, len(i)-1):
                    if abs(i[j] - i[j+1]) <= k:
                        return True
        return False


        

if __name__ == "__main__":
    # nums[0] == nums[3], abs(0-3) <= 3 : True
    # print(Solution().containsNearbyDuplicate([1,2,3,1], 3))

    # nums[0] == nums[3], abs(0-3) <= 2  ==> False
    print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2))