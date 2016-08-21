import random
import os
import time
import pygame

game = [[0 for i in range(34)] for j in range(32)]

class Structure:

	def __init__(self, height, width):
		self.height = height;
		self.width = width;

	def createbox(self):

		for i in range(self.height+2):
			for j in range(self.width+2):

				if (i==0 and j==0) or (i==0 and j == self.width+1) or (i==self.height+1 and j==0) or (i == self.height+1 and j == self.width+1) :
					game[i][j] = '+'

				elif i == 0 and j >= 1 and j <= self.width:
					game[i][j] = '-'

				elif i == self.height+1 and j >=1 and j <= self.width:
					game[i][j] = '-'

				elif j == 0 and i >= 1 and i <= self.height:
					game[i][j] = '|'

				elif j == self.width+1 and i >= 1 and i <= self.height:
					game[i][j] = '|'

				else:
					game[i][j] = ' '


	

class Gameplay:

	def __init__(self):
		self.blocks = [['X', 'X', 'X', 'X'], [['X', 'X'], ['X', 'X']], [['X', 'X'], [' ', 'X', 'X']], [[' ', 'X', 'X'], ['X', 'X']], [[' ', 'X'], ['X', 'X', 'X']], 
						[['X', 'X', 'X'], [' ', ' ', 'X']]]

	def pickRandomBlock(self):
		#return self.blocks[random.randrange(0,6)] #return array of between index of 0 to 5
		return self.blocks[0]

	def assignPosition(self, block, line, index):

		remIndex = index;
		if len(block) == 4: #1D - Array
			for i in block:
				game[line][index] = i;
				index +=1

		else: # 2-D Array
			for i in block:
				for j in i:
					if game[line][index] != 'X':
						game[line][index] = j
					index += 1
				line += 1
				index = remIndex


	def deassignPosition(self, index, block, line):
		remIndex = index
		if len(block) == 4:
			for i in block:
				game[line][index] = ' '
				index += 1
		else:
			for i in block:
				for j in i:
					if j == 'X':
						game[line][index] = ' '
					index += 1
				line += 1
				index = remIndex



	def move1Unit(self, index, block, line):
		self.deassignPosition(index, block, line-1)
		if(self.checkNextPosition(block, line, index)):
			self.assignPosition(block, line, index)
			#print "block moved"
			return 'target moved'
		else:
			self.assignPosition(block, line-1, index)
			#print "block not moved"
			return 'target blocked'


class Board(Gameplay):

	def __init__(self):
		Gameplay.__init__(self)


	def checkNextPosition(self, block, line, index):
		remIndex = index

		if line == 30 and len(block) != 4:
			return False

		elif line == 31 and len(block) == 4:
			return False

		elif len(block) == 4:
			for i in block:
				if game[line][index] == 'X':
					return False
				else:
					index += 1
			return True		

		else:	
			for i in block:
				for j in i:
					if game[line][index] == 'X' and j == 'X':
						return False
					else:
						index += 1

				line += 1
				index = remIndex

			return True

	def checkRowFull(self):
		for i in range(1, 33):
			if game[30][i] == ' ':
				return False
		
		return True

	def ClearRow(self):
		if self.checkRowFull():
			#print "clear roew onnnnnnnnnnnnnnnn!!!!!!!!!!!!!!"
			for i in range(30, 0, -1):
				if i != 1:
					for j in range(1, 33):
						game[i][j] = game[i-1][j]

				else:
					for j in range(1, 33):
						game[1][j] = ' '

			if self.checkRowFull():
				self.ClearRow()			


class Block(Board):

	def __init__(self):
		Board.__init__(self)

	def moveright(self, block, line, index):

		self.deassignPosition(index, block, line)
		if(self.checkNextPosition(block, line, index+1)):
			self.assignPosition(block, line, index+1)
			return 'target moved'
		else:
			self.assignPosition(block, line, index)
			return 'target blocked'

	def moveleft(self, block, line, index):

		self.deassignPosition(index, block, line)
		if(self.checkNextPosition(block, line, index-1)):
			self.assignPosition(block, line, index-1)
			return 'target moved'
		else:
			self.assignPosition(block, line, index)
			return 'target blocked'






def printbox():
	for i in game:
		for j in i:
			print j,
		print




Tetris = Structure(30, 32);
brick = Board()
tile = Block()
Tetris.createbox()

game[30][1] = 'X'
for i in range(6, 33, 1):
	game[30][i] = 'X'

os.system('clear')

while True:
	block = brick.pickRandomBlock()

	index = 2
	if(brick.checkNextPosition(block, 1, index)):
		brick.assignPosition(block, 1, index)
		printbox()


	s=2
	blockStatus = 'target moved'

	while True:
		time.sleep(.03)
		os.system('clear')
		if blockStatus == 'target moved' and s <= 30:
			blockStatus = brick.move1Unit(index, block, s)

			brick.ClearRow()
			printbox()

		
			s+=1
		else:
			break



print '\n\n\n'



