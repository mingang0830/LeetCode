class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        for i in range(x // 2 + 1):
            if (i+1) * (i+1) > x >= i * i:
                return i


print(Solution().mySqrt(4))
