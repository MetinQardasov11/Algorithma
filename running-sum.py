class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum_list = []
        
        for i in nums: # i = 1, 
            num = i + sum_list[-1] if sum_list else i # 1, 3, 6, 10
            sum_list.append(num) # [1, 3, 6, 10]
        
        return sum_list

s = Solution()
print(s.runningSum([1,2,3,4]))
print(s.runningSum([1,1,1,1,1]))
print(s.runningSum([3,1,2,10,1]))