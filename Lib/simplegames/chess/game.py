from pieces import *

class Board:
	
	def __init__(self, white_type, black_type):
		self.white = Player(1, white_type)
		self.black = Player(-1, black_type)
		self.board = self.init_board()
		
	def __str__(self):
		board_string = ''
		for row in self.board:
			board_string += ' '.join([str(c) for c in row])
			board_string += '\n'
		return board_string
		
	def init_board(self):
		board = [self.black.pieces[:8], self.black.pieces[8:]]
		for _ in range(4):
			board.append([Empty() for _ in range(8)])
		board.extend([self.white.pieces[:8], self.white.pieces[8:]])
		return board

class Player:
	
	def __init__(self, player_value, player_type):
		self.value = player_value
		self.player_type = player_type
		self.pieces = self.place_pieces()
		self.score = sum([int(p) for p in self.pieces])
		
	def __repr__(self):
		return f'{self.value}, {self.score}'
		
	def place_pieces(self):
		pawn_row = [Pawn(self.value, i) for i in range(8)]
		noble_row = [Rook(self.value, 0), Bishop(self.value, 1), 
			Knight(self.value, 2), Queen(self.value), King(self.value), 
			Knight(self.value, 5), Bishop(self.value, 6), 
			Rook(self.value, 7)]
		if self.value == 1:
			pawn_row.extend(noble_row)
			return pawn_row
		noble_row.extend(pawn_row)
		return noble_row

class Chess(Board):
	
	def __init__(self, white_type='user', black_type='ai'):
		super().__init__(white_type, black_type)
		self.current_player = self.white
		
	def __iter__(self):
		self.turn = 0
		return self
		
	def __next__(self):
		self.turn += 1
		self.current_player = self.change_player()
		
	def change_player(self):
		if self.current_player is self.black: return self.white
		return self.black
		
	def play(self):
		game = iter(self)
		while self.turn < 10:
			# white turn
			next(game)
			# black turn
		return self.turn


if __name__ == '__main__':
	game = Chess()
