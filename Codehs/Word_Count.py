# text = input()
# my_list = text.split()
# dic1 = {}
# for word in my_list:
#     count_dictionary = my_list.count(word)
#     dic1[word] = count_dictionary
# print(dic1)

def update_counts(count_dictionary, word):
    word = input()
    my_list = word.split()
    dic1 = {}
    for item in my_list:
        count = my_list.count(item)
        dic1[item] = count
    print(dic1)
    
update_counts(4, "a turtle on a fence had help")
update_counts(4, "")