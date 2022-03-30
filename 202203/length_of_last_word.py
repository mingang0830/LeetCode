class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.split()[-1])
        if len(s) == 1:
            return 1

        str_: str = s[::-1]
        count: int = 0

        for i in range(len(s)):
            if str_[i] == " ":
                pass
            else:
                count += 1
                if i+1 == len(s) or str_[i+1] == " ":
                    return count





print(Solution().lengthOfLastWord("abc "))