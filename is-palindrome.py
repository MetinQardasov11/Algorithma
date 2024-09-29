class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''.join(char.lower() for char in s if char.isalnum())
        
        if new_str == new_str[::-1]:
            return True
        else:
            return False

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(" "))
print(s.isPalindrome("0P"))