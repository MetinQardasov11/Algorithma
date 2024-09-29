class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        return sum(all(char in allowed for char in word) for word in words)

s = Solution()
print(s.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))
print(s.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))