class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al").replace("G", "G")

s = Solution()
print(s.interpret("G()(al)"))
print(s.interpret("G()()()()(al)"))
print(s.interpret("(al)G(al)()()G"))