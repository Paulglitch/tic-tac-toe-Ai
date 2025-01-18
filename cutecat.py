

import random

#function to print the board 

def print_board(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8]) 
    
#function to check if a player has won

def check_win(board, player):
    return ((board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player)) 
    
#function to check if the board is full 

def check_full(board):
    return ' ' not in board

#function to get the player's move

def player_move(board):
    move = int(input('Enter your move (0-8): '))
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print('Invalid move. Try again.')
        player_move(board)
        
#function to get the ai's move

def ai_move(board):
    move = random.randint(0, 8)
    if board[move] == ' ':
        board[move] = 'O'
    else:
        ai_move(board)
        
#function to play the game 

def play_game():
    board = [' '] * 9
    print_board(board)
    while True:
        player_move(board)
        print_board(board)
        if check_win(board, 'X'):
            print('You win!')
            break
        if check_full(board):
            print('It\'s a tie!')
            break
        ai_move(board)
        print_board(board)
        if check_win(board, 'O'):
            print('AI wins!')
            break
        if check_full(board):
            print('It\'s a tie!')
            break
            
def save_wins():
    #save the wins to a file
    with open('wins.txt', 'a') as file:
        file.write('AI\n')        

def learn_game():
    #read the wins from the file
    with open('wins.txt', 'r') as file:
        wins = file.readlines()
    #create a dictionary to store the moves
    moves = {}
    #iterate over the wins
    for win in wins:
        #split the win into a list of moves
        win = win.strip()
        win = win.split(',')
        #iterate over the moves
        for i in range(len(win) - 1):
            #get the current move
            current_move = win[i]
            #get the next move
            next_move = win[i + 1]
            #check if the current move is in the dictionary
            if current_move in moves:
                #check if the next move is in the dictionary
                if next_move in moves[current_move]:
                    #increment the count of the next move
                    moves[current_move][next_move] += 1
                else:
                    #add the next move to the dictionary
                    moves[current_move][next_move] = 1
            else:
                #add the current move to the dictionary
                moves[current_move] = {next_move: 1}
    #return the dictionary
    return moves
#play the game

play_game() 
