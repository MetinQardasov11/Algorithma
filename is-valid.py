class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        for c in s:
            if c in "({[":
                stack.append(c)
            elif c == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif c == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif c == "}" and stack and stack[-1] == "{":
                stack.pop()
            else:
                return False
        return not stack
        

s = Solution()
print(s.isValid("()[]{}"))
print(s.isValid("([)]"))