import random


#our board in dictionary form
board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '
    	}

g_numx_win = 0
g_numo_win = 0
g_num_tie = 0
g_times = 0
g_turn = ['X', 'O']    	
 	
#print our board
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] + '\n')
        
#check for X/O WIN, there are 8 possibilities=3row + 3col + 2diag    
def check_win(board, turn):
	if ((board['top-L'] == turn and board['top-M'] == turn and board['top-R'] == turn) 
	or (board['low-L'] == turn and board['low-M'] == turn and board['low-R'] == turn) 
	or (board['mid-L'] == turn and board['mid-M'] == turn and board['mid-R'] == turn) 
	or (board['top-L'] == turn and board['mid-L'] == turn and board['low-L'] == turn) 
	or (board['top-M'] == turn and board['mid-M'] == turn and board['low-M'] == turn) 
	or (board['top-R'] == turn and board['mid-R'] == turn and board['low-R'] == turn) 
	or (board['top-L'] == turn and board['mid-M'] == turn and board['low-R'] == turn) 
	or (board['top-R'] == turn and board['mid-M'] == turn and board['low-L'] == turn)):
		return True
	else:
		return False

def reset_board():
	global board
	board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '
    	}

def is_tie():
	#check for TIEs, i.e. no empty space in the board.
	tie_game = True
	for key in board.keys():
		if board[key] == " ": #check for empty spot on the board
			tie_game = False
			break

	if tie_game:
		return True
	else:
		return False


def computer_version(board):
	random.seed()

	global g_turn
	i = 0
	set_turn = 0
	#'X' starts
	turn = g_turn[0]

	while True:
		global g_numx_win
		global g_numo_win
		global g_num_tie
		move = random.choice(list(board.keys()))
		#need to first check if the space is already taken or not.
		if set_turn == 1:	#if the item has been setted
			turn = g_turn[i % 2] #then turn the Character 'X' => 'O' or 'O' => 'X'
			set_turn = 0	#And reset set_turn as 0

		if board[move] == " ":
			board[move] = turn #set this item as turn ('X' or 'O')
			set_turn = 1	#And set set_turn as 1
			i += 1	#move i to next(such as: 1, 2, 3...)
			

		if check_win(board, 'X'):
			g_numx_win += 1
			print('X wins!\n')
			break
			
		if check_win(board, 'O'):
			g_numo_win += 1
			print('O wins!\n')
			break
			
		if is_tie():
			g_num_tie += 1
			print('Tie!\n')
			break				

def main():
	global g_times
	g_times += 1
	print("------------------------------------")
	print("g_times: " + str(g_times) + '\n')
	
	reset_board()	#reset the board
	computer_version(board)
	printBoard(board)
	print("Number of X wins: " + str(g_numx_win))
	print("Number of O wins: " + str(g_numo_win))
	print("Number of TIEs: " + str(g_num_tie))
	# print("\n------------------------------------\n\n")


for j in range(50000):
	main()		


print("\n===============================")
print("Total Number of X wins: " + str(g_numx_win))
print("Total Number of O wins: " + str(g_numo_win))
print("Total Number of TIEs: " + str(g_num_tie) + '\n')
print("Tic tac toe is not a fair game, the one who starts first is almost " + 
"twice more likely to win.")


