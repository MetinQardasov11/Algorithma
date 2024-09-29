class Solution:
    def mySqrt(self, x: int) -> int:
        square_root = pow(x, 0.5)
        return int(square_root)

s = Solution()
print(s.mySqrt(4))
print(s.mySqrt(8))