class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        if len(nums)>0:
            for i in range(len(nums)):
                if nums.count(nums[i]) == 1:
                    return nums[i]
        else:
            return 0

s = Solution()
print(s.singleNumber([2,2,1]))
print(s.singleNumber([4,1,2,1,2]))
print(s.singleNumber([1]))