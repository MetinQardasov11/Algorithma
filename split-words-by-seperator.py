class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        
        new_list = []
        for i in range(len(words)):
            words[i] = words[i].split(separator)
            for j in range(len(words[i])):
                if words[i][j] == '':
                    continue
                new_list.append(words[i][j])
        return new_list
        
s = Solution()
print(s.splitWordsBySeparator(["one.two.three","four.five","six"], '.'))
print(s.splitWordsBySeparator(["$easy$", "$problem$"], '$'))
print(s.splitWordsBySeparator(["|||"], '|'))