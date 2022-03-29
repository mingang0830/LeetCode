from typing import Dict

"""
roman_num: Dict = {"I": 1,
                   "V": 5,
                   "X": 10,
                   "L": 50,
                   "C": 100,
                   "D": 500,
                   "M": 1000}

four_or_nine: Dict = {"IV": 4,
                      "IX": 9,
                      "XL": 40,
                      "XC": 90,
                      "CD": 400,
                      "CM": 900}


class Solution:
    def romanToInt(self, s: str) -> int:
        result: int = 0
        temp: str = s

        for i in range(len(s) - 1):
            two_chars = s[i] + s[i + 1]
            if two_chars in four_or_nine.keys():
                result += four_or_nine[two_chars]
                temp = temp.replace(two_chars, "")

        for j in temp:
            result += roman_num[j]
        return result
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        map_: Dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum_: int = 0
        for i in range(len(s)):
            if i + 1 < len(s) and map_[s[i]] < map_[s[i + 1]]:
                sum_ -= map_[s[i]]
            else:
                sum_ += map_[s[i]]
        return sum_
