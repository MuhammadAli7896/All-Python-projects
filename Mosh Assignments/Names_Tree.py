names = ["Zaki", "Shaheer", "ali", "faiq","Mujtba"]
for i in range(len(names)):
    for x in range(i + 1):
        print(names[x], end=" ")
    print()
# names = ["zaki","ali","faiq"]
#
# for x in range(len(names)):
#     if x != 0:
#         print("\n")
#     for i in range(0, x+1):
#         print(names[i],end=" ")