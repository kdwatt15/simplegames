# Standard imports
import sys
import operator
from datetime import datetime

class TicTacToe:
	
	def __init__(self, players=0):
		"""
		:args: players - dictates gametype (0 --> ai v. ai, 1 --> user 
			v. ai, 2 --> user v. user
			
		:param: board - dict of keys 0-8 representing current board state
		:param: current_player - current player to switch between
		:param: player_type - determines whether the computer or manual
			function will be called during gameplay
		"""
		self.players = players
		self.board = self.init_board()
		self.current_player = 1
		if players == 0: 
			self.player_type = 'computer'
		else:
			self.player_type = 'manual'
			
	def __str__(self):
		""" Allows the game to be printed for command line play """
		board = ''
		for index, cell in enumerate(self.board.values()):
			if cell == 1: 
				mark = 'X' 
			elif cell == -1: 
				mark = 'O'
			else:
				mark = ' '
			board += f' {mark} '
			if ((index + 1) % 3 != 0): board += '|'
			if (index + 1) % 3 == 0 and 8 > index > 0:
				board+= '\n-----------\n'
		return board
		
	def init_board(self):
		""" Creates empty dict for the board """
		board = {}
		for i in range(9):
			board[i] = 0
		return board
			
	def change_player(self):
		""" Changes the player type and switches the current player """
		self.__change_player_type()
		if self.current_player == 1:
			self.current_player = -1
		else:
			self.current_player = 1
			
	def __change_player_type(self):
		""" Switches player type based on number of players """
		# don't change from init in two-player/no-player games
		if (self.players in (0, 2)): return False
		if self.player_type == 'manual':
			self.player_type = 'computer'
		else:
			self.player_type = 'manual'
		
	def check_for_tie(self, board):
		""" Checks for playable cells on the board """
		return 0 not in board.values()
			
	def check_for_win(self, board, current_player):
		""" Returns true or false indicating whether the player given
		has won on the board given """
		winning_combos = [
			(0,1,2), (3,4,5), (6,7,8), # horizontal combos
			(0,3,6), (1,4,7), (2,5,8), # vertical combos
			(0,4,8), (2,4,6)           # diagonal combos
		]
		
		for combo in winning_combos:
			owned_cells = [True for x in combo if board[x] == current_player]
			if (len(owned_cells) == 3): return True
		return False
		
	def manual_move(self):
		""" Prompts user for input and executes the move of reprompts 
		the user """
		move = False
		while True:
			x = int(input('x: '))
			y = int(input('y: '))
			board_index = x + (y * 3)
			if self.board[board_index] == 0:
				self.board[board_index] = self.current_player
				break
			
	def return_open_cells(self, board):
		""" Returns open cells on the board """
		return [k for k, v in board.items() if v == 0]
			
	def computer_move(self, minimax=False):
		""" Calls the minimax function to determine computer move """
		ai_move = self.max_move(self.board, self.current_player, 
			minimax=minimax)
		self.board[ai_move[0]] = self.current_player
	
	def max_move(self, board, current_player, alpha=-10, beta=10, 
		minimax=False):
		move_scores = dict.fromkeys(self.return_open_cells(board))
		
		for move in move_scores.keys():
			current_board = board.copy()
			current_board[move] = current_player
			if self.check_for_win(current_board, current_player):
				score = 10
			elif self.check_for_tie(current_board):
				score = 0
			else:
				calc_move = self.min_move(current_board, 
					current_player * -1, alpha, beta, minimax)
				score = calc_move[1]
				if score >= beta and minimax == False: return calc_move
				
			if score > alpha:
				alpha = score
				
			move_scores[move] = score
				
		best_move = list(max(move_scores.items(), 
			key=operator.itemgetter(1)))
			
		return best_move
		
	def min_move(self, board, current_player, alpha=-10, beta=10,
		minimax=False):
		move_scores = dict.fromkeys(self.return_open_cells(board))
		
		for move in move_scores.keys():
			current_board = board.copy()
			current_board[move] = current_player
			if self.check_for_win(current_board, current_player):
				score = -10
			elif self.check_for_tie(current_board):
				score = 0
			else:
				calc_move = self.max_move(current_board, 
					current_player * -1, alpha, beta, minimax)
				score = calc_move[1]
				if score <= alpha and minimax == False: return calc_move
				
			if score < beta:
				beta = score
					
			move_scores[move] = score
				
		best_move = list(min(move_scores.items(), 
			key=operator.itemgetter(1)))
			
		return best_move
		
	def gameplay(self, explicit=True):
		""" Plays the game, calling functions of this class based on the
		current player_type and name of function """
		self.board = self.init_board()
		gameover = ''
		while gameover == '':
			getattr(self, f'{self.player_type}_move')()
			if (explicit): print(self)
			# Return current player if win
			if self.check_for_win(self.board, self.current_player):
				return self.current_player
			# Return 0 if tie
			if (self.check_for_tie(self.board)): 
				return 0
			self.change_player()
		

b = TicTacToe()
