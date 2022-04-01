class Solution:
    def decimal(self, bin_: str) -> int:
        result: int = 0
        i: int = 0
        for j in range(len(bin_)-1, -1, -1):
            if bin_[j] == "0":
                pass
            elif bin_[j] == "1":
                result += 2 ** i
            i += 1
        return result

    def addBinary(self, a: str, b: str) -> str:
        # return format(int(a, 2) + int(b, 2), 'b')
        return format(self.decimal(a) + self.decimal(b), 'b')


print((Solution().addBinary("1010", "1011")))

