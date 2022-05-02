from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        temp: List= []
        while n != 1:
            n =sum([int(i)**2 for i in str(n)])
            if n in temp:
                return False
            else:
                temp.append(n)
        return True

            
            


if __name__ == "__main__":
    print(Solution().isHappy(2))