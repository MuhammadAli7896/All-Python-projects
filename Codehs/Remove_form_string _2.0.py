def remove_all_from_string(word, letter):
    index = word.find(letter)
    quantity = len(letter)
    while index >= 0:
        new_string = word[:index] + word[index+quantity:]
        index = new_string.find(letter)
        if index != -1:
            new2_string = new_string[:index] + new_string[index+quantity:]
            return new2_string
        else:
            return new_string
        # while index == -1:
        #     new_string = word[:index] + word[index+quantity:]
        #     index = word.find(letter)
        #     return new_string
        return new_string       
    return word
print(remove_all_from_string("bananas","na"))