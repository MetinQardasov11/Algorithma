class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1

s = Solution()
print(s.smallestEqual([0,1,2]))
print(s.smallestEqual([4,3,2,1]))
print(s.smallestEqual([1,2,3,4,5,6,7,8,9,0]))