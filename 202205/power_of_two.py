import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        # return n == 1 or (n % 2 == 0 and self.isPowerOfTwo(n // 2))
        
        if n == 1 or n == 2 :
            return True
        elif n == 0 or n % 2 == 1:
            return False
        else:
            return self.isPowerOfTwo(n / 2)

        """
        math domain error 발생!

        return math.log2(n).is_integer()
        """

        
        """
        비트 연산자 사용 풀이법

        return (n & (n-1) == 0) and n != 0
        """

        






print(Solution().isPowerOfTwo(16))
print(math.log(536870912, 2))