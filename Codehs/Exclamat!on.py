# update this function so it replaces all lowercase 'i's in `text` with '!'
def exclamation(text):
    listing = list(text)
    for index, a in enumerate(listing):
        if a == "i":
            listing[index]="!"
    answer = "".join(listing)
    return answer
    
print(exclamation("I like music."))