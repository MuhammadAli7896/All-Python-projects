n = int(input())
l = list(map(int, input().split()))
# if all(l) >0:
#     if any(l) == reversed(str(any(l))):
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)
print(all(i > 0 for i in l) and any(str(j) == str(j)[::-1] for j in l))