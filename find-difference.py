class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        difference = list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))
        return difference

s = Solution()
print(s.findDifference([1,2,3], [2,4,6]))
print(s.findDifference([1,2,3,3], [1,1,2,2]))