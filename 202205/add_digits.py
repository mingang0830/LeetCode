class Solution:
    def addDigits(self, num: int) -> int:
        if(num < 10):
            return num
        
        temp_num: int = 0
        while(num > 0):
            temp_num += num%10
            num = num//10            
            
        return self.addDigits(temp_num)

if __name__ == "__main__":
    print(Solution().addDigits(38))