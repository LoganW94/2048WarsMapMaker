import pygame

# colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)

class Cursor:
	
	def __init__(self, screen):
		self.screen = screen
		self.counter = 0
		self.is_clicked = False
		self.wait = False
		self.timer = 0
		self.visible = False

	def update(self, mouse_pos, z):
		self.mouse_pos = mouse_pos
		self._z = z
		
		if self.wait == True:
			self.timer +=1
			if self.timer == 10:
				self.timer = 0
				self.wait = False

		if self.is_clicked == True:	
			self.blink()		

	def clicked(self):
		if self.visible == False and self.wait == False:
			self.is_clicked = True
			self.wait = True
		elif self.visible == True and self.wait == False:
			self.clicked = False			

	def blink(self):	
		if self.counter <= 5:
			self.visible = False
			self.counter +=1
		elif self.counter <= 10:
			self.visible == True
			self.counter += 1
		else:
			self.counter = 0

	def draw(self,mouse_pos):	
		x = 20
		y = 20
		if self.visible == True:
			self.screen.fill(black, rect = ((x, y), (1, 11)))