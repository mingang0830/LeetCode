from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # return [str(format(i, 'b')).count("1") for i in range(n+1)]
        
        result = []
        for i in range(n+1):
            sum = 0
            num = i
            
            while num != 0:
                sum += num%2
                num = num//2
            
            result.append(sum)
        
        return result
