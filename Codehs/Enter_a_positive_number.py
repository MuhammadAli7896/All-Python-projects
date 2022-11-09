def retrieve_positive_number():
    positive_number = int(input("Enter a number: "))
    try:
        while positive_number > 0:
            positive_number = int(input("Enter a number: "))
            return positive_number
    except ValueError:
        if positive_number <= 0:
            print("Please Enter a nautural number.")

print(retrieve_positive_number())