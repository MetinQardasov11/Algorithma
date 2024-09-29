class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                if heights[i] < heights[j]:
                    heights[i], heights[j] = heights[j], heights[i]
                    names[i], names[j] = names[j], names[i]
        return names


s = Solution()
print(s.sortPeople(["Mary","John","Emma"], [180, 165, 170]))
print(s.sortPeople(["Alice","Bob","Bob"], [155, 185, 150]))