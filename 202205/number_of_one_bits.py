class Solution:
    def hammingWeight(self, n: int) -> int:
        # return str(bin(n)).count("1")
        count: int = 0
        while (n):
            n &= n-1
            count+= 1
        
        return count

if __name__ == "__main__":
    print(Solution().hammingWeight(0b00000000000000000000000000001011))