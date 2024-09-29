class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        
        max_word = 0
        for sentence in sentences:
            number_of_word = len(sentence.split(' '))
            if number_of_word > max_word:
                max_word = number_of_word
        
        return max_word

s = Solution()
print(s.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
print(s.mostWordsFound(["please wait", "continue to fight", "continue to win"]))