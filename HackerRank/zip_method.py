n,x = map(int, input().split())
b = []
for i in range(x):
    a= list(map(float, input().split()))
    b.append(a)
for item in zip(*b):
    print(round(sum(item)/len(item),1))