class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ""
            

s = Solution()
print(s.firstPalindrome(["abc","car","ada","racecar","cool"]))
print(s.firstPalindrome(["notapalindrome","racecar"]))
print(s.firstPalindrome(["def","ghi"]))