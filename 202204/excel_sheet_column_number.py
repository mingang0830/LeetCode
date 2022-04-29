char_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"]

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result: int = 0
        for i, c in enumerate(reversed(columnTitle)):
            result += (26**i) * (char_list.index(c) + 1)
        return result


if __name__ == "__main__":
    print(Solution().titleToNumber("A"))