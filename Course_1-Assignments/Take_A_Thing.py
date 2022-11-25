def remove_sort_reverse(my_list):
    # perform operations on `my_list` to 
    # 1. remove all "eggplant"s
    # 2. sort it
    # 3. reverse it!
    how_many = my_list.count("eggplant")
    for i in range(how_many):
        my_list.remove("eggplant")
    my_list.sort()
    my_list.reverse()
    return my_list