def get_valid_index(prompt):
    while True:
        try:
            index = int(input(prompt))
            if index >= 0 and index <= 2:
                return index
            print("Must be 0 - 2 inclusive!")
        except ValueError:
            print("Must be an integer!")
    return

# game_is_over
# -----
# Return True if the game is over and False
# otherwise. Print a message indicating who
# won or whether there was a tie.
def game_is_over(board):
    for i in range(3):
        # Check horizontal
        if board[i][0] == board[i][1] == board[i][2] \
            and board[i][0] != " ":
            print_board(board)
            print(board[i][0] + " wins!")
            return True
        
        # Check vertical
        if board[0][i] == board[1][i] == board[2][i] \
            and board[0][i] != " ":
            print_board(board)
            print(board[0][i] + " wins!")
            return True
        
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] \
        and board[0][0] != " ":
        print_board(board)
        print(board[0][0] + " wins!")
        return True
    
    if board[2][0] == board[1][1] == board[0][2] \
        and board[2][0] != " ":
        print_board(board)
        print(board[2][0] + " wins!")
        return True
    
    # Check tie
    if " " not in board[0] and " " not in board[1] \
        and " " not in board[2]:
        print_board(board)
        print("Tie game!")
        return True
    
    # Not over yet!
    return False

def print_board():
    one = 'X' if xstate[0] else ('O' if zstate[0] else 1)
    two = 'X' if xstate[1] else ('O' if zstate[1] else 2)
    three = 'X' if xstate[2] else ('O' if zstate[2] else 3)
    four = 'X' if xstate[3] else ('O' if zstate[3] else 4)
    five = 'X' if xstate[4] else ('O' if zstate[4] else 5)
    six = 'X' if xstate[5] else ('O' if zstate[5] else 6)
    seven = 'X' if xstate[6] else ('O' if zstate[6] else 7)
    eight = 'X' if xstate[7] else ('O' if zstate[7] else 8)
    nine = 'X' if xstate[8] else ('O' if zstate[8] else 9)
    # if xstate[0]: # for one
    #     one = 'X'
    # elif zstate[0]:
    #     one = 'O'
    # else:
    #     one= 1
    # if xstate[1]: # for two
    #     two = 'X'
    # elif zstate[1]:
    #     two = 'O'
    # else:
    #     two = 2
    # if xstate[2]: # for three
    #     three = 'X'
    # elif zstate[2]:
    #     three = 'O'
    # else:
    #     three = 3
    # if xstate[3]: # for four
    #     four = 'X'
    # elif zstate[3]:
    #     four = 'O'
    # else:
    #     four = 4
    # if xstate[4]: # for five
    #     five = 'X'
    # elif zstate[4]:
    #     five = 'O'
    # else:
    #     five = 5
    # if xstate[5]: # for six
    #     six = 'X'
    # elif zstate[5]:
    #     six = 'O'
    # else:
    #     six = 6
    # if xstate[6]: #for seven
    #     seven = 'X'
    # elif zstate[6]:
    #     seven = 'O'
    # else:
    #     seven = 7
    # if xstate[7]: # for eight
    #     eight = 'X'
    # elif zstate[7]:
    #     eight = 'O'
    # else:
    #     eight = 8
    # if xstate[8]: # for nine
    #     nine = 'X'
    # elif zstate[8]:
    #     nine = 'O'
    # else:
    #     nine = 9
    print(f"{one} | {two} | {three} ")
    print(f"--|---|---")
    print(f"{four} | {five} | {six} ")
    print(f"--|---|---")
    print(f"{seven} | {eight} | {nine} ") 
    
xstate = [0,0,0,0,0,0,0,0,0]
zstate = [0,0,0,0,0,0,0,0,0]
turn = 0
print_board()
while True:
    #turn = 0
    #print_board()
    if turn % 2 == 0:
        print("It's 'X' turn.")
        X_turn = int(input("Enter a number (1-9): "))
        turn += 1
        if xstate[X_turn - 1] == 'O':
            print("Enter another value.")
            continue
        else:
            xstate[X_turn - 1] = True
            print_board()
    elif turn %2 == 1:
        print("It's 'O' turn.")
        Z_turn = int(input("Enter a value (1-9): "))
        turn += 1
        if zstate[Z_turn - 1] == 'X':
            print("Enter another value.")
            continue
        else:
            zstate[Z_turn - 1] = True
            print_board()
    else:
        continue