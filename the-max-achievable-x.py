class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        max = 0
        
        if num > t or num == t or num < t:
            max = num + t + t
        
        return max

s = Solution()
print(s.theMaximumAchievableX(num=1, t=1))
print(s.theMaximumAchievableX(num=4, t=1))
print(s.theMaximumAchievableX(num=3, t=2))
print(s.theMaximumAchievableX(num=1, t=2))