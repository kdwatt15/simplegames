from random import shuffle

class Card:
	value_names = {
		0: 'joker',
		1: 'ace',
		2: 'two',
		3: 'three',
		4: 'four',
		5: 'five',
		6: 'six',
		7: 'seven',
		8: 'eight',
		9: 'nine',
		10: 'ten',
		11: 'jack',
		12: 'queen',
		13: 'king'
	}
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
		self.name = self.value_names[self.value]
		
	def __str__(self):
		if self.suit == 'joker': return 'Joker'
		return f'{self.name.title()} of {self.suit.title()}s'

class Deck:
	suits = ('spade', 'heart', 'club', 'diamond')
	def __init__(self, exclusions=None, shuffle=True, jokers=False):
		self.deck = self.ordered_deck(jokers)
		self.strip_deck(exclusions)
		if shuffle: self.shuffle()
		
	def __len__(self):
		return len(self.deck)
		
	def ordered_deck(self, jokers):
		deck = []
		if jokers: deck.extend([Card('joker', 0) for _ in range(2)])
		for suit in self.suits:
			deck.extend([Card(suit, i+1) for i in range(13)])
		return deck
		
	def strip_deck(self, exclusions):
		""" Removes exlusions from full deck """
		pass
		
	def shuffle(self):
		""" Randomizes order of the deck """
		shuffle(self.deck)
		
	
				
