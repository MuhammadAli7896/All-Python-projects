my_float = 3.3312

# Your code here...
while True:
    guess = float(input("Enter a guess: "))
    if round(guess,2) > round(my_float,2):
        print("Too high!")
        continue
    elif round(guess,2) < round(my_float,2):
        print("Too low!")
        continue
    elif round(guess,2) == round(my_float,2):
        print("Correct!")
        break
    else:
        break