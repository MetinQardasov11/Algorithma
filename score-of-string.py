class Solution:
    def scoreOfString(self, s: str) -> int:
        
        sum_num = 0
        for i in range(len(s)-1):
            num = abs(ord(s[i])-ord(s[i+1]))
            sum_num += num
        
        return sum_num
            
        

s = Solution()
print(s.scoreOfString("hello"))
print(s.scoreOfString("zaz"))