class Solution:
    def reverseBits(self, n: int) -> int:
        
        len_n: int = 32
        result: int =0
        for i in range(len_n):
            # 이진수로 만들고 바로 reverse된 위치의 10진수로 전환
            result += n%2 * (2**(len_n-i-1))
            n //= 2
        return result

if __name__ == "__main__":
    print(Solution().reverseBits(0b0101))
