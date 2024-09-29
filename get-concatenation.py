class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums * 2

s = Solution()
print(s.getConcatenation([1,2,1]))
print(s.getConcatenation([1,3,2,1]))