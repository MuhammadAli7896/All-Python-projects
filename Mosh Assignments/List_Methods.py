numbers = [0, 10, 29, 38, 11, 28, 92, 30, -200, 9, 20, 33, 57, -38, 48, 45, 72, -20, -39, 4, 22, 91, 38, 66, -66, 4, 55, 6, -33, 94, 30]
# To find location of element in list
location: int = numbers.index(max(numbers))
print(location)

location2: int = numbers.index(min(numbers))
print(location2)

# to reverse the series
numbers.reverse()
print(numbers)

# to count how many times a number is in the series
print(numbers.count(80))

# Write the maximum number
print(max(numbers))

# Sort the numbers in ascending order
numbers.sort()
print('List in Ascending Order: ', numbers)

# Sort the numbers in descending order
numbers.sort(reverse=True)
print('List in Descending Order: ', numbers)

# to sum numbers in the series
print(sum(numbers[23:-2]))
print(sum(numbers[:3]))

# How many numbers are in the list
print(len(numbers))

# To remove duplicates use set operator
# like [*set(name of list)]
# idher * is lie hai k wo run mein curly brackets htadey list mein se