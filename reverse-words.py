class Solution:
    def reverseWords(self, s: str) -> str:
        
        list_word = s.split()
            
        return ' '.join(map(lambda x: x[::-1], list_word))
        
        

s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))