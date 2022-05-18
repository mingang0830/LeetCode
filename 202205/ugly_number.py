class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0 :
            return False
        
        if n % 2 == 0:
            if n // 2 == 1: 
                return True
            else: 
                return self.isUgly(n // 2)
        elif n % 3 == 0:
            if n // 3 == 1: 
                return True
            else: 
                return self.isUgly(n // 3)
        elif n % 5 == 0:
            if n // 5 == 1: 
                return True
            else: 
                return self.isUgly(n // 5)
        else:
            return False


if __name__ == "__main__":
    print(Solution().isUgly(6)) # True
    print(Solution().isUgly(1)) # True
    print(Solution().isUgly(0)) # False