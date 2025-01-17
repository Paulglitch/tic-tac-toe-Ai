

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
#play the game

play_game() 
