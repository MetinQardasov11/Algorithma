class Solution:
    def finalValueAfterOperations(self, operations: list) -> int:
        x = 0
        for i in operations:
            if i == "--X" or i == "X--":
                x -= 1
            else:
                x += 1
        return x

s = Solution
print(s.finalValueAfterOperations(s, ["--X","X++","X++"]))
print(s.finalValueAfterOperations(s, ["++X","++X","X++"]))
print(s.finalValueAfterOperations(s, ["X++","++X","--X","X--"]))