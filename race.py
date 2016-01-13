from tools import *

class Race(object):
	def __init__(self):
		self.race_name = "none"
		self.lot_race = {"Human":10, "Dwarf":2, "Elf": 2, "Half-elf":1, "Half-orc":1, "Dragonborn":1, "Gnome":1, "Halfling":1, "Teifling":1}
	
	def race_ability_modifier(self, race):
		if race_name == "Dwarf":
			self.CON += 2
	
	def menu_race_select(self):
		race_var = raw_input("Please select a race:\n\n\t[a] Dawrf\n\t[b] Dragonborn\n\t[c] Elf\n\t[d] Gnome\n\t[e] Halfling\n\t[f] Half-Elf\n\t[g] Half-Orc\n\t[h] Human\n\t[i] Tiefling\n\t[r] Random\n\n>>: ")
		if race_var.lower() == "a":
			self.race_name = "Dwarf"
		elif race_var.lower() == "b":
			self.race_name = "Dragonborn"
		elif race_var.lower() == "c":
			self.race_name = "Elf"
		elif race_var.lower() == "d":
			self.race_name = "Gnome"
		elif race_var.lower() == "e":
			self.race_name = "Halfling"
		elif race_var.lower() == "f":
			self.race_name = "Half-Elf"
		elif race_var.lower() == "g":
			self.race_name = "Half-Orc"
		elif race_var.lower() == "h":
			self.race_name = "Human"
		elif race_var.lower() == "i":
			self.race_name = "Teifling"
		elif race_var.lower() == "r":
			self.race_name = lot(self.lot_race)
		else:
			self.race_name = "none"

x = Race()

x.menu_race_select()

print x.race_name
