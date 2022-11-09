import random
words = ["muhammad", "apple", "Pakistan", "America", "Korea", "Afghanistan", "Argentina", "Belgium", "Croatia", "Netherlands", "Slovakia", "Venezuela"]
#words = ["muhammad", "apple"]
secret_word = random.choice(words).lower()
secret_word2 = secret_word
dashes = "-" * len(secret_word)
print(dashes)
print("You have 10 guesses")

def get_guess():
    guesses_left = 10
    #secret_word = random.choice(words).lower()
    #secret_word2 = secret_word
    current_dashes_state = "-" * len(secret_word2)
    while guesses_left > 0:
        guess = input("Guess: ")
        if len(guess) != 1:
            print("Your guess must have exactly one character!")
            continue
        if not guess.islower():
            print("Your guess must be a lowercase letter!")
            continue
        if not guess in secret_word2:
            print("That letter is not in the secret word!")
            guesses_left = guesses_left - 1
            current_dashes_state = update_dashes(secret_word2, current_dashes_state, guess)
            if guesses_left == 0:
                break
            print(current_dashes_state)
            print(f"{guesses_left} incorrect guesses left.")
            continue
        if guess in secret_word2 and guess.islower() and len(guess) ==1:
            print("That letter is in the secret word!")
            guesses_left = guesses_left
            current_dashes_state = update_dashes(secret_word2, current_dashes_state, guess)
            print(current_dashes_state)
            if current_dashes_state == secret_word2:
                print(f"Congrats! You win. The word was: {current_dashes_state}")
                #break
                break
            print(f"{guesses_left} incorrect guesses left.")
            continue
    if current_dashes_state != secret_word2:
        print(f"You lose. The word was: {secret_word2}")
    return current_dashes_state

def update_dashes(secret_word2, current_dashes_state, guess):
    my_list = list(current_dashes_state)
    for i in range(len(secret_word2)):
        if secret_word2[i] == guess:
            my_list[i] = guess
    new_state = "".join(my_list)
    return new_state
    

guess1 = get_guess()
# while True:
#     if guess1 == secret_word2:
#         print(f"Congrats! You win. The word was: {secret_word2}")
#         break
#     if guess1 != secret_word2:
#         print(f"You lose. The word was: {secret_word2}")
#         break
