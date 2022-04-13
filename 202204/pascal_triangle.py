from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result: List[List[int]] = []
        row: List[int] = [1]
        a: List[int] = [0]
        for x in range(numRows):
            result.append(row)
            # [1,1,0], [0,1,1] -> [1,2,1]
            row = [left + right for left, right in zip(row + a, a + row)]
        return result


if __name__ == "__main__":
    print(Solution().generate(5))
