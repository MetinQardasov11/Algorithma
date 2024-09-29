class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            if endTime[i] >= queryTime >= startTime[i]:
                count += 1
        return count

s = Solution()
print(s.busyStudent([1,2,3], [3,7,7], 4))
print(s.busyStudent(startTime = [4], endTime = [4], queryTime = 4))