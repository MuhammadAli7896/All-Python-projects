def get_index():
    while True:
        # integer validation
        try:
            index = int(input("Enter a index (-1 to quit): "))
            while index + 1 > len(initial) or index < -1:
                print("invalid index.")
                index = int(input("Enter a index (-1 to quit): "))
        except ValueError:
           print("Not an integer! Try again.")
           continue
        else:
           return index 
           break
    # while index + 1 > len(initial) or index < -1:
    #     print("invalid index.")
    #     index = int(input("Enter a index (-1 to quit): "))
    return index
        #index = int(input("Enter a index (-1 to quit): "))

    

def get_letter():
    # alphabet validation
    while True:
        try:
            letter = input("Enter a letter: ")
            while letter.isupper():
                print("Character must be a lowercase letter!")
                letter = input("Enter a letter: ")
            while len(letter) > 1:
                print("Must be exactly one character!")
                letter = input("Enter a letter: ")
        except ValueError:
            print("Not an alphabet! Try again.")
            continue
        else:
            return letter
            break
    return letter
    
initial = input("Enter a word: ")

while True:
    index = get_index()
    if index == -1:
        break
    letter = get_letter()
    listing = list(initial)
    listing[index] = letter
    word = "".join(listing)
    print(word)
    while True:
        index2 = get_index()
        if index2 == -1:
            break
        letter2 = get_letter()
        listing2 = list(word)
        listing2[index2] = letter2
        word = "".join(listing2)
        print(word)
    if index2 == -1:
        break