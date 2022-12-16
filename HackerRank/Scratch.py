# Palindromic triangle with nested loops
for i in range(1,int(input())+1):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
    print()
    
    

