class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        if len(s_list) == len(pattern) and len(set(s_list)) == len(set(pattern)) == len(set(zip(s_list,pattern))):
            return True
        else:
            return False

if __name__=="__main__":
    print(Solution().wordPattern("aba","dog cat cat"))