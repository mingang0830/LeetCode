from typing import Dict, List

class Solution:
    def int_ver(self, s: str) -> List[int]:
        dict_: Dict[str,int] = {}
        result: List[int] = []
        for i, v in enumerate(list(dict.fromkeys(s))): # list(dict.fromkeys(s)) -> s의 중복 문자 제거 후 리스트로 반환
            dict_[v] = i
        
        for j in s:
            result.append(dict_[j])
        return result

    def isIsomorphic(self, s: str, t: str) -> bool:
        if self.int_ver(s) == self.int_ver(t):
            return True
        else:
            return False
        

if __name__ == "__main__":
    print(Solution().isIsomorphic('paper','title'))