class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        '''
        if needle in haystack:
            return len(haystack.split(needle)[0])
        '''

        if needle in haystack:
            div: int = len(needle)
            for idx in range(0, len(haystack)):
                temp: str = haystack[idx:div]
                if temp == needle:
                    return idx
                div += 1
        return -1



