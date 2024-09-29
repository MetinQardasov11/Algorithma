class Solution:
    def countPairs(self, nums: list, target: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1
        return count
        
s = Solution()
print(s.countPairs([-1,1,2,3,1], 2))
print(s.countPairs(nums = [-6,2,5,-2,-7,-1,3], target = -2))