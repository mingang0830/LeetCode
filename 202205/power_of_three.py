class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        
        while n % 3 == 0:
            n /=  3
            
        return n == 1

        # In Java, maximum value of type of signed integer is 2147483647
        # so the maximum value of n that is a power of three is 1162261467 
        # return n > 0 and 1162261467 % n == 0