class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count
    
s = Solution()
print(s.findNumbers([12,345,2,6,7896]))
print(s.findNumbers([555, 901, 482, 1771]))