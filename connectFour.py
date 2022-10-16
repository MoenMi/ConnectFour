# Connect 4, Michael Moen

# board is a 2D array that stores the current state of the game board
board = [ [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0] ]

# an array of all vaild rows to place a piece
eligible_moves = ['1', '2', '3', '4', '5', '6', '7']

# tracks the highest available spot in each column
highest_eligible = [0, 0, 0, 0, 0, 0, 0]

player1 = True      # tracks which player's turn it is
player1_char = 'I'  # the character used by player1
player2_char = 'X'  # the character used by player2
turn_counter = 0    # number of current turn
winner = 'none'     # set to player1_char or player2_char upon victory
ongoing = True      # True when neither player has won

def displayBoard():

    print('\n1  2  3  4  5  6  7')
    print('-------------------')

    for r in range(len(board)-1, -1, -1):
        for c in range(len(board[r])):
            print(board[r][c], end='  ')
        print()
    print()

def playerMove(player_char):

    global turn_counter, player1, player1_char, player2_char, ongoing     #allows the function to use global variables
    turn_counter += 1
    
    displayBoard()
    
    print(f"Player {player1_char if player1 else player2_char}'s turn:")
    
    move = input('Enter a move: ')
    while not move in eligible_moves:
        print(f'Invalid move, choose one of the following rows: {eligible_moves}')
        move = input('Enter a move: ')
    move = int(move)
    
    board[highest_eligible[move-1]][move-1] = player_char
    highest_eligible[move-1] += 1
    if highest_eligible[move-1] > 5:
        eligible_moves.remove(str(move))
    if checkVictory(highest_eligible[move-1]-1, move-1):
        ongoing = False

# Checks for 4 consecutive instances of the character of the played (num_in_line)
# Arguments row and column store the position of the most recent move
def checkVictory(row, column):

    global winner

    # target_char is the character of the player who just made a move
    target_char = player1_char if (turn_counter % 2 == 1) else player2_char

    #horizontal check
    num_in_line = 1     # number of target_char, if >= 4, the player wins
    dist = 1            # stores current distance from the position of the player's move
    while column + dist < len(board[row]):
        if board[row][column+dist] == target_char:
            num_in_line += 1
            print(num_in_line)
            dist += 1
        else:
            break
    dist = 1
    while column - dist >= 0:
        if board[row][column-dist] == target_char:
            num_in_line += 1
            dist += 1
        else:
            break
    if num_in_line >= 4:
        winner = target_char
        return True

    #vertical check
    num_in_line = 1
    dist = 1
    while row + dist < len(board):
        if board[row+dist][column] == target_char:
            num_in_line += 1
            dist += 1
        else:
            break
    dist = 1
    while row - dist >= 0:
        if board[row-dist][column] == target_char:
            num_in_line += 1
            dist += 1
        else:
            break
    if num_in_line >= 4:
        winner = target_char
        return True

    #diag-up-right
    num_in_line = 1
    dist = 1
    while column + dist < len(board[row]) and row + dist < len(board):
        if board[row+dist][column+dist] == target_char:
            num_in_line += 1
            dist += 1
        else:
            break
    dist = 1
    while column - dist >= 0 and row - dist >= 0:
        if board[row-dist][column-dist] == target_char:
            num_in_line += 1
            dist += 1
        else:
            break
    if num_in_line >= 4:
        winner = target_char
        return True

    #diag-down-right
    num_in_line = 1
    dist = 1
    while column + dist < len(board[row]) and row - dist >= 0:
        if board[row-dist][column+dist] == target_char:
            num_in_line += 1
            dist += 1
        else:
            break
    dist = 1
    while column - dist >= 0 and row + dist < len(board):
        if board[row+dist][column-dist] == target_char:
            num_in_line += 1
            dist += 1
        else:
            break
    if num_in_line >= 4:
        winner = target_char
        return True

    return False

# Main Code Sequence
print("Welcome to Connect 4 Python\n")
print(f"Player {player1_char} moves first, Player {player2_char} moves second")
while ongoing and turn_counter < 42:

    if player1:
        playerMove(player1_char)
    else:
        playerMove(player2_char)
    player1 = not player1

displayBoard()
if winner != 'none':
    print(f'Congratulations Player {winner}, you won in {turn_counter} turns!')
else:
    print('The game ended with no victor :(')