char_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"]


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result: str = ""
        while columnNumber != 0:
            q, r = divmod(columnNumber - 1, len(char_list))
            temp: str = char_list[r]
            result = temp + result
            columnNumber = q
        return result


if __name__ == "__main__":
    print(Solution().convertToTitle(701))
