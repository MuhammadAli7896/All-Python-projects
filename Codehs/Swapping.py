# swap_lists
# -----
# This function takes two lists of equal length 
# as arguments and swaps their values.
def swap_lists(first, second):
    # Write your code here...
    list_three = []
    for item in first:
        list_three.append(item)
    for i in range(len(first)):
        first[i] = second[i]
    for j in range(len(second)):
        second[j] = list_three[j]
    

list_one = [1, 2, 3]
list_two = [4, 5, 6]

print("Before swap")
print("list_one: " + str(list_one))
print("list_two: " + str(list_two))

swap_lists(list_one, list_two)

print("After swap")
print("list_one: " + str(list_one))
print("list_two: " + str(list_two))