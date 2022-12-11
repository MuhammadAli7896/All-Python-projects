n = int(input())
s = set(map(int, input().split()))
commands = int(input())
for i in range (commands):
    t = input().split()
    if 'remove' in t:
        s.remove(int(t[-1]))
    elif 'discard' in t:
        s.discard(int(t[-1]))
    elif 'pop' in t:
        s.pop()
print(sum(s))
