class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)


s = Solution()
print(s.fib(2))
print(s.fib(3))
print(s.fib(4))
print(s.fib(5))