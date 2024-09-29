def top_k_elements(arr: list, k):
    
    arr.sort()
    return arr[-k:]

print(top_k_elements([1, 5, 3, 2, 4], 3))