import re
from typing import List, Pattern


class Solution:
    def isPalindrome(self, s: str) -> bool:
        parse: Pattern[str] = re.compile('[a-zA-Z0-9]')
        s_lst: List = [char.lower() for char in parse.findall(s)]
        temp: List = []

        for i in s_lst:
            temp.insert(0, i)

        if s_lst == temp:
            return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().isPalindrome("ab_a"))
