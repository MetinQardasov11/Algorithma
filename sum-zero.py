class Solution:
    def sumZero(self, n: int) -> list[int]:
        return [i for i in range(1, n) if i != n//2]

s = Solution()
print(s.sumZero(5))
print(s.sumZero(3))
print(s.sumZero(1))