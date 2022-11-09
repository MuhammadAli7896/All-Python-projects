def remove_all_from_string(word, letter):
    index = word.find(letter)
    while index >= 0:
        new_string = word[:index] + word[index+1:]
        if index != -1:
            new_string = word[:index] + word[index+1:]
        else:
            return new_string
        return new_string        
    return word
remove_all_from_string("pancakes","i")
