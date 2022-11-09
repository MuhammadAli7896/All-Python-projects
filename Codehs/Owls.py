# this function should return the number of words that contain "owl"!
def owl_count(text):
    text_x = text.lower()
    listing = text_x.split()
    #listing = list(test_x)
    key = "owl"
    word = 0
    my_list = []
    for index, i in enumerate(listing):
        if key in i:
            word = word + 1
            my_list.append(index)
    print(f"There were {word} words that contained 'owl'.")
    print(f"They occurred at indices: {my_list} " )
owl_count("Pooh's friend is a wise old Owl")
owl_count("Owls are so cool! I think snowy owls might be my favorite. Or maybe spotted owls.")
owl_count("I really like owls. Did you know that an owl's eyes are more than twice as big as the eyes of other birds of comparable weight? And that when an owl partially closes its eyes during the day, it is just blocking out light? Sometimes I wish I could be an owl")