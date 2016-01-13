from tools import *
from race import *

class Character(object):
	def __init__(self):
		self.STR = 0
		self.RB_STR = 0 #RB = Race Bonus
		self.DEX = 0
		self.RB_DEX = 0
		self.CON = 0
		self.RB_CON = 0
		self.INT = 0
		self.RB_INT = 0
		self.WIS = 0
		self.RB_WIS = 0
		self.CHA = 0
		self.RB_CHA = 0
		
		self.HP_MAX = 0
		
		self.gender = "none"
		
		self.character_name = "none"
		self.race_name = "none"
		self.class_name = "none" #Class level, experience points
		
		self.axis = "none" #Lawful, nuetral, chaotic
		self.alignment = "none" #Good, neutral, evil
		
		self.age_title = "none"
		self.age = 0
	
	def fc_gender(self):
		gender_var = raw_input("Choose a gender:\n\n\t[F]emale\n\t[M]ale\n\t[R]andom\n\n>>: ")
		if gender_var.lower() == "f":
			self.gender = "Female"
		elif gender_var.lower() == "m":
			self.gender = "Male"
		elif gender_var.lower() == "r":
			var = d(1,2)
			if var == 1:
				self.gender = "Female"
			elif var == 2:
				self.gender = "Male"
		else:
			self.gender = "none"
	
	def fc_RB_reset(): #resets race bonus to 0
		self.RB_STR = 0
		self.RB_DEX = 0
		self.RB_CON = 0
		self.RB_INT = 0
		self.RB_WIS = 0
		self.RB_CHA = 0
	
	def fc_race_dwarf(self):
		self.race_name = "Dwarf"
		self.RB_CON += 2
	
	def fc_age_title(self):
		age_title_var = raw_input("Select the age group of the NPC:\n\n\t[B]aby\n\t[Y]outh\n\t[M]iddle Age\n\t[E]lder\n\t[R]andom\n\n>>: ")
		if age_title_var.lower() == "b":
			self.age_title = "Baby"
		elif age_title_var.lower() == "y":
			self.age_title = "Youth"
		elif age_title_var.lower() == "m":
			self.age_title = "Middle Age"
		elif age_title_var.lower() == "e":
			self.age_title = "Elder"
		elif age_title_var.lower() == "r":
			var = d(1,100)
			if var <= 5:
				self.age_title = "Baby"
			elif var > 5 and var <= 25:
				self.age_title = "Youth"
			elif var > 25 and var <= 85:
				self.age_title = "Middle Age"
			elif var > 85:
				self.age_title = "Elder"
		else:
			self.age_title = "none"
	
	def fc_race(self):
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
			pass
		else:
			self.race_name = "none"
	
	def fc_stat_roll(self): #Manual entry, roll, ask if stats would like to be kept.
		num = 3
		if self.age_title == "Baby":
			num = 1
		elif self.age_title == "Youth":
			num = 2
		elif self.age_title == "Middle Age":
			num = 3
		elif self.age_title == "Elder":
			num = 2
		else:
			num = 3
		
		self.STR += d(num, 6)
		self.DEX += d(num, 6)
		self.CON += d(num, 6)
		self.INT += d(num, 6)
		self.WIS += d(num, 6)
		self.CHA += d(num, 6)

	def fc_name(self, name="none"):
		if name == "none":
			self.name = raw_input("What is your name?\n\n>>: ")
			print self.name
		else:
			self.name = name
			print name

	def print_char(self):
		print "Character Name:", self.character_name
		print "Race:", self.race_name
		print "Class/Occupation:", self.class_name
		print "Age Title:", self.age_title
		print "Gender:", self.gender
		print " "
		print "Character Stats:", "\n"
		print "\tSTR:", self.STR
		print "\tDEX:", self.DEX
		print "\tCON:", self.CON
		print "\tINT:", self.INT
		print "\tWIS:", self.WIS
		print "\tCHA:", self.CHA
		print "\n\n"

#x = Character()

#while x.race_name == "none":
#	x.fc_race()

#while x.age_title == "none":
#	x.fc_age_title()

#while x.STR == 0:
#	x.fc_stat_roll()

#x.print_char()
