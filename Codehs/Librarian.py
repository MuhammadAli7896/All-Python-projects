names = []
for i in range(5):
    name = input("Name: ")
    listing = name.split()
    names.append(listing[-1])
names.sort()
print(names)