class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        n_str = str(n)
        
        odd_index_num = []
        even_index_num = []
        for i in range(len(n_str)):
            if i % 2 == 0:
                even_index_num.append(int(n_str[i]))
            else:
                odd_index_num.append(int(n_str[i]))
                
        return (sum(odd_index_num) - sum(even_index_num)) * (-1)
        
    
s = Solution()
print(s.alternateDigitSum(521))
print(s.alternateDigitSum(111))
print(s.alternateDigitSum(886996))