def guess(num: int, pick: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    elif num == pick:
        return 0

class Solution:
    def guessNumber(self, n: int, pick: int) -> int:
        high = n
        low = 1
        while low<=high:
            mid = low +(high-low)//2
            
            if guess(mid, pick)==0:
                return mid
            if guess(mid, pick)==-1:
                high = mid-1
            else:
                low = mid+1
        return mid



print(Solution().guessNumber(10, 6))