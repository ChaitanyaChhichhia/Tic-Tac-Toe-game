# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 23:41:30 2021
Description: Tic Tac Toe game using python
@author: Chaitanya Chhichhia
"""
import random

lst=[1,2,3,4,5,6,7,8,9]
lst_str_demo=['1','2','3','4','5','6','7','8','9']  #list used in the demo
# lst_board=[" "," "," "," "," "," "," "," "," "]  #main list which will store the markers
lst_board=[]


def intro(lst):
    print("Welcome to Tic Tac Toe!! \n")
    print("RULES- Each player chosses a marker among X or O")
    print("The game ends when either the board is full or a player is successfully able to get his markers in a line.")
    print("The following board shows the available positions on the board- \n")
    print("   |   |   ")
    print(" {} | {} | {}".format(lst_str_demo[6], lst_str_demo[7], lst_str_demo[8]))
    print("   |   |   ")
    print("------------")
    
    print("   |   |   ")
    print(" {} | {} | {}".format(lst_str_demo[3], lst_str_demo[4], lst_str_demo[5]))
    print("   |   |   ")
    print("------------")
    
    print("   |   |   ")
    print(" {} | {} | {}".format(lst_str_demo[0], lst_str_demo[1], lst_str_demo[2]))
    print("   |   |   ")
    
    print("\nEnjoy the game!!\n")


def display_board(lst_board):
    for i in range (1,10):
        print()
    print("   |   |   ")
    print(" {} | {} | {}".format(lst_board[6], lst_board[7], lst_board[8]))
    print("   |   |   ")
    print("------------")
    
    print("   |   |   ")
    print(" {} | {} | {}".format(lst_board[3], lst_board[4], lst_board[5]))
    print("   |   |   ")
    print("------------")
    
    print("   |   |   ")
    print(" {} | {} | {}".format(lst_board[0], lst_board[1], lst_board[2]))
    print("   |   |   ")
   
     
def player_input():       #decided the markers chosed by players
    player1_marker=''
    while (player1_marker!='X' and player1_marker!='O'):
        player1_marker=input('player 1 choose X or O\t:')
    
    if player1_marker=='X':
        player2_marker='O'
    else:
        player2_marker='X'
    return (player1_marker,player2_marker)
  
      
def place_marker(lst_board, marker, position):  # assign position to the marker in string
    lst_board[position]=marker
 
    
def win_check(board, mark):     #returns false if no one has won
    if ((board[0]==mark and board[1]==mark and board[2]==mark) or 
        (board[3]==mark and board[4]==mark and board[5]==mark) or 
        (board[6]==mark and board[7]==mark and board[8]==mark) or 
        (board[0]==mark and board[3]==mark and board[6]==mark) or 
        (board[1]==mark and board[4]==mark and board[7]==mark) or 
        (board[2]==mark and board[5]==mark and board[8]==mark) or 
        (board[0]==mark and board[4]==mark and board[8]==mark) or
        (board[2]==mark and board[4]==mark and board[6]==mark)  ):
        #print('{} wins'.format(mark))
        return True     
    else:
        return False
    

def choose_first():  # chooses which player goes first
    n=random.randint(1,2)
    if n==1:
        print('Player 1 goes first')
    else :
        print('Player 2 goes first')
    return n


def space_check(lst_board, position):    #returns true if the particular position is empty
     return lst_board[position-1]==" "


def full_board_check(lst_board):   #returns true if board is full
    for i in range (0,9):
        if lst_board[i]==" ":
            return False
        else:
            pass
    return True
# =============================================================================
# 
# def get_input_position(lst):
#     
#     n='wrong'
#     
#     while not n.isdigit() or n not in lsts:
#         n=input("Please enter your position (1-9): ")
#         
#         if n.isdigit():
#             if n not in lsts:
#                 print("The number should be between 1-9")
#             else:
#                 pass
#         else :
#             print('Please enter a numeric value: ')
#             
#     return int(n)
# 
# =============================================================================
 
def player_choice (lst_board, lst_str_demo, player):    #returns the position chosen by player
    position='wrong'
    while position=='wrong' :
        position=input("Please enter your position {}: " .format(player))
        if position.isdigit():
            if position in lst_str_demo:
                if space_check(lst_board, int(position)):
                    return int(position)
                else:
                    print ('The position is already taken')
                    position='wrong'
            else:
                print ('Please enter a value between 1 to 9')
                position='wrong'
        else:
            print ('Please enter a numeric value')
            position='wrong'                  

        
def replay(wins_by_player1,wins_by_player2):
    r=input("Hope you enjoyed the game, would you like to play again? y/n: ")
    while r not in ['Y','y','N','n']:
        r=input("Please enter a character among Y,y,N,n: ")
    if r in ['n','N']:
        if (wins_by_player1>wins_by_player2):
            print("Player 1 wins the tournament")
        else:
            print("Player 2 wins the tournament")
    return r in ['y','Y']

    
def position_assign(position,lst_board,marker):
    lst_board[position-1]=marker
   
    
def game_on(lst_board, player1_marker, player2_marker):   #returns true if game is on
    if (full_board_check(lst_board)):
        return False
    if win_check(lst_board, player1_marker):
        return False
    if win_check(lst_board, player2_marker):
        return False
    return True
    

def main():
    wins_by_player1=0
    wins_by_player2=0
    total_games=0
    replay_var=True
    
    intro(lst_str_demo)
    
    while (replay_var):
        lst_board=[" ",]*9
        
                #deciding the marker of each player
        player1_marker, player2_marker = player_input()  #tuple unpacking
        print ("Player-1 chose {}, Player-2 chose {}" .format(player1_marker, player2_marker))
        
                #deciding which player goes first
        player1_turn=choose_first()
        
        while game_on(lst_board, player1_marker, player2_marker):   
                #game continues till the board is not full or someone wins
            if (player1_turn==1):
                position=player_choice(lst_board, lst_str_demo, "Player1")
                position_assign(position, lst_board, player1_marker)
                display_board(lst_board)
                if not (game_on(lst_board, player1_marker, player2_marker)):
                    if (win_check(lst_board, player1_marker)):
                        print("Player 1 won the game")
                        wins_by_player1+=1
                    else:
                        print("Both played well, the match is a draw")
                    break
                else:
                    pass
                    # break
                position=player_choice(lst_board, lst_str_demo, "Player2")
                position_assign(position, lst_board, player2_marker)
                display_board(lst_board)
                if not (game_on(lst_board, player1_marker, player2_marker)):
                    if (win_check(lst_board, player2_marker)):
                        print("Player 2 won the game")
                        wins_by_player2+=1
                        
                    else:
                        print("Both played well, the match is a draw")
                    break
                else:
                    pass
                # break
            else:
                position=player_choice(lst_board, lst_str_demo, "Player2")
                position_assign(position, lst_board, player2_marker)
                display_board(lst_board)
                if not (game_on(lst_board, player1_marker, player2_marker)):
                    if (win_check(lst_board, player2_marker)):
                        print("Player 2 won the game")
                        wins_by_player2+=1
                    else:
                        print("Both played well, the match is a draw")
                    break
                else:
                    pass
                    # break
                position=player_choice(lst_board, lst_str_demo, "Player1")
                position_assign(position, lst_board, player1_marker)
                display_board(lst_board)
                if not (game_on(lst_board, player1_marker, player2_marker)):
                    if (win_check(lst_board, player1_marker)):
                        print("Player 1 won the game")
                        wins_by_player1+=1
                    else:
                        print("Both played well, the match is a draw")
                    break
                else:
                    pass
                    # break
        total_games+=1
        print("Total games played : {}".format(total_games))   
        print("Scores till now-")   
        print("Player 1 : {}".format(wins_by_player1))
        print("Player 2 : {}".format(wins_by_player2))
        replay_var=replay(wins_by_player1,wins_by_player2)
        
        
main()
