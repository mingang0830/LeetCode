from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result: List[List[int]] = []
        row: List[int] = [1]
        a: List[int] = [0]
        for x in range(rowIndex+1):
            result.append(row)
            row = [left + right for left, right in zip(row + a, a + row)]
        return result[rowIndex]


if __name__ == "__main__":
    print(Solution().getRow(3))