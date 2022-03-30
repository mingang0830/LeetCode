from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        한줄로 만들기 -> 가독성 별로..
        메소드 가독성도 신경을 써야하나?

        return [int(digit) for digit in str(int("".join(map(str, digits))) + 1)]
        """

        str_digits: str = "".join(map(str, digits))
        integer: int = int(str_digits) + 1
        return [int(digit) for digit in str(integer)]

