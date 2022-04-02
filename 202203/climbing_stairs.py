class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2

        step1: int = 1
        step2: int = 2
        cur: int = 0
        for i in range(3, n+1):
            cur = step1 + step2
            step1 = step2
            step2 = cur
        return cur

print(Solution().climbStairs(4))