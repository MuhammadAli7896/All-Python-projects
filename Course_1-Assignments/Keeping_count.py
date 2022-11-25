# update this function to return the number of times `second` appears in `first`!
def count_occurrences(word, character):
    count = 0
    for i in range(len(word)):
        if word[i] == character:
            count = count + 1
    return count
    
print(count_occurrences("banana","a"))