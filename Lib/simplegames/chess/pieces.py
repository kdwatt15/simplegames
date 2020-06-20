"""
https://www.chess.com/article/view/chess-piece-value

Piece values derived from Bobby Fischer. Credit to Drunk History for
introducing me to a true American hero.
"""

class Empty():
	def __init__(self):
		self.value = 0
		self.letter = '--'
		
	def __str__(self):
		return self.letter

class Piece:
	
	def __init__(self, player, x, value, letter):
		# player will be used for movement
		self.player = player
		self.x = x
		if player == 1: self.y = 7
		else: self.y = 0
		self.value = value
		
		# letter is for CLI play
		self.letter = letter
		
	def __str__(self):
		if self.player == 1: 
			color = 'w'
		elif self.player == -1:
			color = 'b'
		return f'{color}{self.letter}'
		
	def __int__(self):
		return self.value

class Pawn(Piece):
	
	def __init__(self, player, x):
		super().__init__(player, x, 4, 'P')
		self.y -= player
		self.moved = False
		
	def move_range(self, board):
		rng = self.capture_range(board)
		y = self.y
		x = self.x
		i = 0
		while True:
			y-=self.player
			if board[y][x] == '--':
				rng.append((x, y))
			else:
				return rng
			if self.moved or y == self.player * -2 + self.y:
				return rng
				
		return rng
		
	def capture_range(self, board):
		rng = []
		y = self.y - self.player
		x = self.x
		for diag in (-1, 1):
			if board[y][x + diag].value == - self.player:
				rng.append((y, x + diag))
		return rng
		
	def move(self, board, x, y):
		if (x, y) in self.move_range():
			self.x = x
			self.y = y
			return True
		return False
	
class Knight(Piece):
	
	def __init__(self, player, x):
		super().__init__(player, x, 12, 'K')
		
class Bishop(Piece):
	
	def __init__(self, player, x):
		super().__init__(player, x, 13, 'B')
		
class Rook(Piece):
	
	def __init__(self, player, x):
		super().__init__(player, x, 20, 'R')
		
class Queen(Piece):
	
	def __init__(self, player, x=3):
		super().__init__(player, x, 38, 'Q')
		
class King(Piece):
	
	def __init__(self, player, x=4):
		super().__init__(player, x, 0, 'X')
		
