alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n = int(input())
for i in range(n):
    print(" " * i,end="")
    # for s in range(i):
    #     print(" ")
    for k in range(i,n,1):
        print(alpha[k],end= "")
    for j in range(n-2,i-1,-1):
        print(alpha[j],end="")
    print()
    