class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        negative_abs = set()
        
        for num in nums:
            if num < 0:
                negative_abs.add(abs(num))
        
        max_num = -1
        for num in nums:
            
            if num > max_num and num in negative_abs:
                max_num = num
        
        return max_num
        
            
        

s = Solution()
print(s.findMaxK([-1,2,-3,3]))
print(s.findMaxK([-1,10,6,7,-7,1]))
print(s.findMaxK([-10,8,6,7,-2,-3]))
