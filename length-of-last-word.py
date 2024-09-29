class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strs = s.split()
        
        if not strs:
            return 0
        else:
            return len(strs[-1])

s = Solution()
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("   fly me   to   the moon  "))
print(s.lengthOfLastWord('luffy is still joyboy'))