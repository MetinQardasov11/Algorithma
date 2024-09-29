class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        
        len_list = len(nums)
        
        for i in range(len_list+1):
            if i not in nums:
                return i

s = Solution()
print(s.missingNumber([3,0,1]))
print(s.missingNumber([0,1]))
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))