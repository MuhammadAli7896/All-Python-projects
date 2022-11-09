arr = []
N = int(input())

for _ in range(N):
    name = input().split()
    # name[ 'first word of input'] ['second is number of input'] ['third is number of imput'] 
        #check input if name['append'] == 'append' go to next
    if name[0] == 'append':
        # arr.append(int( ['second is number of input']))  int ()-> convert to integer
        arr.append(int(name[1]))  
    if name[0] == 'insert':
        arr.insert(int(name[1]), int(name[2]))
    if name[0] == 'remove':
        arr.remove(int(name[1]))
    if name[0] == 'sort':
        arr.sort()
    if name[0] == 'pop':
        arr.pop()
    if name[0] == 'reverse':
        arr.reverse()
    if name[0] == 'print':
        print(arr)
