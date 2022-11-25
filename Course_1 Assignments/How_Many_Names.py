number_of_names = int(input("How many names do you have? : "))
first_name = input("What's your first name? : ")
my_string = " "
for i in range(number_of_names - 2):
    middle_name = input("Middle name: ")
    my_string = my_string + middle_name +" "
last_name = input("What's your last name? : ")
print(first_name + my_string + last_name)