class Solution:
    def findWordsContaining(self, words: list, x: str) -> list[int]:
        
        index_list = []
        
        for index, char in enumerate(words):
            if x in char:
                index_list.append(index)
        
        return index_list
                
                

s = Solution()
print(s.findWordsContaining(["leet","code"], "e"))
print(s.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "a"))
print(s.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "z"))