class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row_str = {}
        row = 0
        row_switch = True
        result = ''

        for char in s:
            # {0:'pahn', 1:'aplsiig', 2:'yir'}
            if row not in row_str: 
                row_str[row] = char
            else:
                row_str[row] += char

            if row == 0:
                row_switch = True
            elif row == numRows - 1: # 현재 행이 끝 행이면 위로(-1) 전환
                row_switch = False
            
            if row_switch:
                row+=1
            else:
                row-=1
        
        for v in row_str.values():
            result += v
        
        return result