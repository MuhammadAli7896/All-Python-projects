list_of_strings = ["a", "2", "7", "zebra"]
# def safe_int(list_of_strings):
#     for i in range(len(list_of_strings)):
#         try:
#             new_list = [int(item) for item in list_of_strings]
#             return new_list
#         except:
#             if list_of_strings[i].isnumeric() == True:
#                 x = list_of_strings[i]
#                 list_of_strings[i] = int(x)
#             else:
#                 x = 0
#                 list_of_strings[i] = int(x)
#     print(list_of_strings)  # 👉️ [10, 20, 30, 40] 
# safe_int(list_of_strings)




# x = 0
# new = [int(item) if item.isnumeric() == True else item == x  for item in list_of_strings ]   
# print(new)

for i in range(len(list_of_strings)):
    if list_of_strings[i].isnumeric() == True:
        x = list_of_strings[i]
        list_of_strings[i] = int(x)
    else:
        x = 0
        list_of_strings[i] = int(x)




# print(list_of_strings)
def safe_int(list_of_strings):
    for i in list_of_strings:
        if list_of_strings[i].isnumeric() == False:
            list_of_strings[i]=0
    print(list_of_strings)
    
safe_int(list_of_strings)