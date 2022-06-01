class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        start = 0
        end = num
        while start <= end:
            mid = (start + end) // 2
            if mid*mid == num:
                return True
            if mid*mid < num:
                start = mid + 1
            else:
                end = mid - 1
        return False


print(Solution().isPerfectSquare(14))