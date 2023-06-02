if __name__ == '__main__':
    N = int(input())
result = []
for n in range(0,N):
    com = input().split()
    if com[0] == 'insert':
        result.insert(int(com[1]), int(com[2]))
    elif com[0] == 'print':
        print(result)
    elif com[0] == 'remove': 
        result.remove(int(com[1]))
    elif com[0] == 'append':    
        result.append(int(com[1]))
    elif com[0] == 'sort':   
        result.sort()
    elif com[0] == 'pop':
        result.pop()
    elif com[0] == 'reverse':
        result.reverse()



  