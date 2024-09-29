def is_polindrom(num):
    
    num_str = str(num)
    
    for i in range(len(num_str)):
        if num_str[i] != num_str[-i-1]:
            return False

    return True
print(is_polindrom(129999921))