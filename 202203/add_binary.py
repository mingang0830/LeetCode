class Solution:
    def decimal(self, bin_: int) -> int:
        result: int = 0
        bin_temp: str = str(bin_)[::-1]
        for i in range(len(bin_temp[::-1])):
            if bin_temp[i] == "0":
                pass
            elif bin_temp[i] == "1":
                result += 2 ** i

        return result

    def addBinary(self, a: str, b: str) -> str:
        # return format(int(a, 2) + int(b, 2), 'b')
        return format(self.decimal(int(a)) + self.decimal(int(b)), 'b')




