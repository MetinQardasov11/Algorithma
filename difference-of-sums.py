class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum_not_divisible = 0
        sum_divisible = 0

        for i in range(1, n + 1):
            if i % m == 0:
                sum_divisible += i
            else:
                sum_not_divisible += i

        return sum_not_divisible - sum_divisible
        

s = Solution()
print(s.differenceOfSums(10, 3))
print(s.differenceOfSums(5, 6))
print(s.differenceOfSums(5, 1))