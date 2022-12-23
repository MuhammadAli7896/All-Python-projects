# Palindromic triangle with nested loops
for i in range(1,int(input())+1):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
    print()
    
print()
n = int(input()) 
m = n
for i in range(0,m+1):
    for j in range(0,n+1):
        print(" ",end="")
    n -=1
    for j in range(1,i+1):
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
    for j in range(i-1,0,-1):
        print(" ",end="")
    print()

