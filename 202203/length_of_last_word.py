class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.split()[-1])
        if len(s) == 1:
            return 1

        s: str = s[::-1]
        count: int = 0

        for i in range(len(s)):
            if s[i] == " ":
                pass
            else:
                count += 1
                if i+1 == len(s) or s[i+1] == " ":
                    return count





print(Solution().lengthOfLastWord("abc "))