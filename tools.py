#tools.py Rename utilities?

from random import randint
from random import choice

#Die Roll
def d(num, sides):
	result = 0
	for x in range(num):
		result += randint(1, sides)
	return result

#Lottery
def lot(lot_dict):
	choices = []
	for name, lots in lot_dict.iteritems():
		for i in range(lots):
			choices.append(name)
	print choices
	return choice(choices)
