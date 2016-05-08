import random

winning_pieces = int(input("\nNumber of consecutive pieces to terminate the game: ")) 

def run_game():
	rows, columns = get_dimensions()
	board = generate_board(rows, columns)
	play_game(board)

def get_dimensions():
	rows = int(input("\nNumber of rows: "))
	columns = int(input("\nNumber of columns: "))
	return (rows, columns)
	
def play_game(board):
	display_board(board)
	while(True):
		if not winner(board):
			perform_player1turn(board)
			display_board(board)
		else:
			print("\n{}".format(winner(board)))
			return
		if not winner(board):
			perform_player2turn(board) 
			display_board(board)
		else:
			print("\n{}".format(winner(board)))
			return

def display_board(board):
	num_cols = len(board)
	num_rows = len(board[0])
	print('\n')
	border = ('+-' * num_cols) + '+'
	for i in range(num_rows):
		row = [col[i] for col in board]
		print(border)
		for each_elt in row:
			print('{:2}'.format('|' + each_elt), end="")
		print('|')
	print(border)

def winner(board):
	winners = set()
	for each_col in board:
		if decide_winner(each_col):
			winners.add(decide_winner(each_col))
	num_rows = len(board[0])
	for i in range(num_rows):
		row = [col[i] for col in board]
		if decide_winner(row):
			winners.add(decide_winner(row))
	return ("\nPlayer 1 wins!" if winners == {1} else
		   "\nPlayer 2 wins!" if winners == {2} else
		   "\nIt's a tie!" if winners == {1, 2} else None)  
 
def decide_winner(t):
	n = len(t)
	for i in range(n - winning_pieces + 1):
		s = set(t[i: i + winning_pieces])
		if len(s) == 1 and s != {''}:
			return 1 if s == {'x'} else 2
	return None

def generate_board(rows, columns):
	return [['' for i in range(rows)] for j in range(columns)]

def perform_player1turn(board):
	col_chosen = int(input("\nPlayer 1, choose your column: "))
	place_mark('x', board[col_chosen])

def perform_player2turn(board):
	col_chosen = int(input("\nPlayer 2, choose your column: "))
	place_mark('o', board[col_chosen])

# def perform_compturn(board):
#	print("\nComputer's turn...")
#	col_chosen = random.randrange(len(board))
#	place_mark('o', board[col_chosen]) 

def place_mark(mark, column):
	if not all(column):
		for i in reversed(range(len(column))):
			if column[i] == '':
				column[i] = mark
				return
	else:
		del column[len(column) - 1]
		column.insert(0, mark)

run_game()