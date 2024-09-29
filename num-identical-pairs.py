class Solution:
    def numIdenticalPairs(self, nums: list) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    count += 1

        return count

s = Solution()
print(s.numIdenticalPairs([1,2,3,1,1,3]))
print(s.numIdenticalPairs([1,1,1,1]))