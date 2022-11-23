import colorama
from colorama import Back,Fore,Style

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
    one = f'{Fore.LIGHTRED_EX}X{Fore.RESET}' if xstate[0] else (f'{Fore.LIGHTGREEN_EX}O{Fore.RESET}' if zstate[0] else 1)
    two = f'{Fore.LIGHTRED_EX}X{Fore.RESET}' if xstate[1] else (f'{Fore.LIGHTGREEN_EX}O{Fore.RESET}' if zstate[1] else 2)
    three = f'{Fore.LIGHTRED_EX}X{Fore.RESET}' if xstate[2] else (f'{Fore.LIGHTGREEN_EX}O{Fore.RESET}' if zstate[2] else 3)
    four = f'{Fore.LIGHTRED_EX}X{Fore.RESET}' if xstate[3] else (f'{Fore.LIGHTGREEN_EX}O{Fore.RESET}' if zstate[3] else 4)
    five = f'{Fore.LIGHTRED_EX}X{Fore.RESET}' if xstate[4] else (f'{Fore.LIGHTGREEN_EX}O{Fore.RESET}' if zstate[4] else 5)
    six = f'{Fore.LIGHTRED_EX}X{Fore.RESET}' if xstate[5] else (f'{Fore.LIGHTGREEN_EX}O{Fore.RESET}' if zstate[5] else 6)
    seven = f'{Fore.LIGHTRED_EX}X{Fore.RESET}' if xstate[6] else (f'{Fore.LIGHTGREEN_EX}O{Fore.RESET}' if zstate[6] else 7)
    eight = f'{Fore.LIGHTRED_EX}X{Fore.RESET}' if xstate[7] else (f'{Fore.LIGHTGREEN_EX}O{Fore.RESET}' if zstate[7] else 8)
    nine = f'{Fore.LIGHTRED_EX}X{Fore.RESET}' if xstate[8] else (f'{Fore.LIGHTGREEN_EX}O{Fore.RESET}' if zstate[8] else 9)
    print(Fore.LIGHTCYAN_EX)
    print(f"{one} | {two} | {three} ")
    print(f"--|---|---")
    print(f"{four} | {five} | {six} ")
    print(f"--|---|---")
    print(f"{seven} | {eight} | {nine} ") 
    print(Fore.RESET)

def sum(a, b, c):
    return a + b + c

xstate = [0,0,0,0,0,0,0,0,0]
zstate = [0,0,0,0,0,0,0,0,0]

def check_wins(xstate,zstate):
    win = [[1,2,3],[1,4,7],[2,5,8],[3,6,9],[4,5,6],[7,8,9],[1,5,9],[3,5,7]]
    for item in win:
        if xstate[item[0]-1] == True and xstate[item[1]-1] == True and xstate[item[2]-1] == True:
            print("X won the match.")
            return 1
        elif zstate[item[0]-1] == True and zstate[item[1]-1] == True and zstate[item[2]-1] == True:
            print("O won the match.")
            return 0
        else:
            return -1
    

turn = 0
print_board()
while True:
    #turn = 0
    #print_board()
    if turn % 2 == 0:
        print(f"{Fore.LIGHTRED_EX}It's 'X' turn.{Fore.RESET}")
        X_turn = int(input("Enter a number (1-9): "))
        if zstate[X_turn - 1] == True or xstate[X_turn - 1] == True:
            print("Enter another value.")
            continue
        else:
            xstate[X_turn - 1] = True
            print_board()
            turn += 1
            who_win = check_wins(xstate,zstate)
            if who_win != -1:
                print("Match over.")
                break
    elif turn %2 == 1:
        print(f"{Fore.LIGHTGREEN_EX}It's 'O' turn.{Fore.RESET}")
        Z_turn = int(input("Enter a value (1-9): "))
        if xstate[Z_turn - 1] == True or zstate[Z_turn - 1] == True:
            print("Enter another value.")
            continue
        else:
            zstate[Z_turn - 1] = True
            print_board()
            turn += 1
            who_win = check_wins(xstate,zstate)
            if who_win != -1:
                print("Match over.")
                break
    else:
        continue