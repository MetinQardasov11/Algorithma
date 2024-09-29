class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        
        sum_list = 0
        for i in nums:
            sum_list += i
        
        sum_of_digits = 0
        str_digit = ''.join(str(i) for i in nums)
        list_str = list(str_digit)
        
        for i in list_str:
            sum_of_digits += int(i)
        
        return sum_list - sum_of_digits
        
        
        
s = Solution()
print(s.differenceOfSum([1,15,6,3]))
print(s.differenceOfSum([1,2,3,4]))