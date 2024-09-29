if __name__ == '__main__':
    N = int(input())
    
    l = []
    
    for _ in range(N):
        query = input().split()
        
        if query[0] == "insert":
            l.insert(int(query[1]), int(query[2]))
            
        if query[0] == "print":
            print(l)
            
        if query[0] == "remove":
            l.remove(int(query[1]))
            
        if query[0] == "append":
            l.append(int(query[1]))
            
        if query[0] == "sort":
            l.sort()
            
        if query[0] == "pop":
            l.pop()
            
        if query[0] == "reverse":
            l.reverse()