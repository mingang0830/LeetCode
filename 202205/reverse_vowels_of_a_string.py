class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        v_index = []

        for i,v in enumerate(s):
            if v in vowels:
                v_index.append(i)
        
        for j in range(len(v_index)//2):
            s_list[v_index[j]], s_list[v_index[-(j+1)]] = s_list[v_index[-(j+1)]], s_list[v_index[j]]
        
        return ''.join(s_list)
