from subprocess import call as shellcommand
from random import randint as randnum
global board 
global win
global emptyspaces
win = False
board = [["_", "_", "_"],
		 ["_", "_", "_"],
		 ["_", "_", "_"]]
emptyspaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]
		 			   


def game():
	global board
	global win
	while True:
		if win == True:
			return
		print_board(board)
		playergoes()
		computergoes()
		win()



'''def twomoves():
	global board
	fakeboard = []
	for r in board:
		fakeboard.append(r)
	for r in fakeboard:
		for c in r:
			fakeboard[r][c] = "O"'''




		

def checkWin(board):
	global emptyspaces
	for pos in emptyspaces:
		row = int(pos/3)
		col = pos - (row * 3)
		board[row][col] = "O"
		for c in range(0, len(board)):
			if board[0][c] == board[1][c] and board[1][c] == board[2][c] and board[0][c] != "_":
				if board[0][c] == "O":
					emptyspaces.remove(pos)
					return True
		for r in range(0, len(board)):
			if board[r][0] == board[r][1] and board[r][1] == board[r][2] and board[r][0] != "_":
				if board[r][0] == "O":
					emptyspaces.remove(pos)
					return True
		if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "_":
			if board[0][0] == "O":
				emptyspaces.remove(pos)
				return True
		if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != "_":
			if board[2][0] == "O":
				emptyspaces.remove(pos)
				return True
		board[row][col] = "_"
	return False

			
def blockWin():
	global board, emptyspaces
	for pos in emptyspaces:
		row = int(pos/3)
		col = pos - (row * 3)
		board[row][col] = "X"
		for c in range(0, len(board)):
			if board[0][c] == board[1][c] and board[1][c] == board[2][c] and board[0][c] != "_":
				if board[0][c] == "X":
					board[row][col] = "O"
					emptyspaces.remove(pos)
					return True
		for r in range(0, len(board)):
			if board[r][0] == board[r][1] and board[r][1] == board[r][2] and board[r][0] != "_":
				if board[r][0] == "X":
					board[row][col] = "O"
					emptyspaces.remove(pos)
					return True
		if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "_":
			if board[0][0] == "X":
				board[row][col] = "O"
				emptyspaces.remove(pos)
				return True
		if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != "_":
			if board[2][0] == "X":
				board[row][col] = "O"
				emptyspaces.remove(pos)
				return True
		board[row][col] = "_"
	return False

			
	

def print_board(board):
	shellcommand(["clear"])
	for r in board:
		newboard = ""
		i = 0
		for m in r:
			if i == 0:
				newboard += m
				newboard +="|"
			elif i == 1:
				newboard += m
			elif i == 2:
				newboard += "|"
				newboard += m
			i+=1
		print(newboard)
		
def playergoes():
	global board
	global win
	global emptyspaces
	row = input("Which row do you want to play? ")
	row = int(row)
	row-=1
	col = input("Which column do you want to play? ")
	col = int(col)
	col-=1
	if board[row][col] == "_":
		board[row][col] = "X"
		emptyspaces.remove(row * 3 + col)
	else:
		print_board(board)
		print("Sorry that spot is taken go again")
		playergoes()
def computergoes():
	global board
	global win
	global emptyspaces
	if checkWin(board) == False:
		if blockWin() == False:
			row = randnum(0, 2)
			col = randnum(0, 2)
			print(row, col)
			if board[row][col] == "_":
				board[row][col] = "O"
				emptyspaces.remove(row * 3 + col)
			elif len(emptyspaces) > 0:
				computergoes()
def win():
	global board
	global win
	i = 0
	
	if len(emptyspaces) == 0:
		shellcommand(["clear"])
		print("Its a TIE!")
		win = True
	for c in range(0, len(board)):
		if board[0][c] == board[1][c] and board[1][c] == board[2][c] and board[0][c] != "_":
			shellcommand(["clear"])
			if board[0][c] == "X":
				print("Player WINS!")
			else:
				print("Computer WINS!")
			win = True
	for r in range(0, len(board)):
		if board[r][0] == board[r][1] and board[r][1] == board[r][2] and board[r][0] != "_":
			shellcommand(["clear"])
			if board[r][0] == "X":
				print("Player WINS!")
			else:
				print("Computer WINS!")
			win = True
	if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "_":
		shellcommand(["clear"])
		if board[0][0] == "X":
			print("Player WINS!")
		else:
			print("Computer WINS!")
		win = True
	if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != "_":
		shellcommand(["clear"])
		if board[2][0] == "X":
			print("Player WINS!")
		else:
			print("Computer WINS!")
		win = True


game() 
