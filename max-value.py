class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        
        max_value = 0
        for s in strs:
            if s.isdigit():
                max_value = max(max_value, int(s))
            else:
                max_value = max(max_value, len(s))

        return max_value

s = Solution()
print(s.maximumValue(["alic3","bob","3","4","00000"]))
print(s.maximumValue(["1","01","001","0001"]))
print(s.maximumValue(["bs9","j"]))
print(s.maximumValue(["5232","yv","22","c","yawgs","928","4003","2"]))