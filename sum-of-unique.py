class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        sum_unique = 0
        
        for i in nums:
            if nums.count(i) == 1:
                sum_unique += i
        
        return sum_unique

s = Solution()
print(s.sumOfUnique([1,2,3,2]))
print(s.sumOfUnique([1,1,1,1,1]))
print(s.sumOfUnique([1,2,3,4,5]))