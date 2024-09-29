class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        index = word.find(ch)
        if index == -1:
            return word
        else:
            return word[:index+1][::-1] + word[index+1:]

s = Solution()
print(s.reversePrefix("abcdefd", "d"))
print(s.reversePrefix("xyxzxe", "z"))
print(s.reversePrefix("abcd", "z"))