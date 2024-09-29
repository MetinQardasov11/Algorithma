class Solution:
    def minPartitions(self, n: str) -> int:
        
        max = 0
        
        for i in n:
            if int(i) > max:
                max = int(i)
        return max

s = Solution()
print(s.minPartitions("32"))
print(s.minPartitions("82734"))
print(s.minPartitions("27346209830709182346"))