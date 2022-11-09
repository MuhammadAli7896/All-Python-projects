def print_board(board):
    for i in range(len(board)):
        print(" ".join([str(x) for x in board[i]]))

my_grid = []

for i in range(8):
    my_grid.append([0] * 8)
            
# for i in range(len(my_grid)):
#     print(my_grid[i])

for i in range(3):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 1:
            my_grid[i][j] = 1
        elif i % 2 == 1 and j % 2 == 0:
            my_grid[i][j] = 1
        else:
            my_grid[i][j] = 0            
        

for i in range(5,8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 1:
            my_grid[i][j] = 1
        elif i % 2 == 1 and j % 2 == 0:
                my_grid[i][j] = 1
        else:
                my_grid[i][j] = 0 
    
print_board(my_grid)