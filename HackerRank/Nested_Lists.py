if __name__ == '__main__':
    l2 = []
    for _ in range(int(input())):
        l1 = []
        name = input()
        l1.append(name)
        score = float(input())
        l1.append(score)
        l2.append(l1)
#print(l2)
l3 = []
for i in range(len(l2)):
    l3.append(l2[i][1])
s = sorted(set(l3))
n = min(s)
s.remove(n)
for num in s:
    if num == n:
        s.remove(num)
s.sort()
l4 = []
for item in l2:
    if item[1]== s[0]:
        l4.append(item[0])
# l4.sort()
print(*sorted(l4), sep="\n")
#print(*sorted(names_of_second_lowest), sep="\n")