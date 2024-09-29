class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        words = s.split(' ')
        
        return ' '.join(words[:k])

s = Solution()
print(s.truncateSentence("Hello how are you Contestant", 4))
print(s.truncateSentence(s = "What is the solution to this problem", k = 4))
print(s.truncateSentence(s = "chopper is not a tanuki", k = 5))