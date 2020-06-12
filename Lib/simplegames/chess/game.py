class Chess:
	
	def __init__(self):
		self.board = self.init_board()
		
	def __str__(self):
		board_string = ''
		for row in self.board:
			board_string+=', '.join(row)
			board_string+='\n'
		return board_string

	def init_board(self):
		board = []
		for _ in range(9):
			row = []
			for _ in range(9):
				row.append('0')
			board.append(row)
		return board

if __name__ == '__main__':
	game = Chess()
