#import pygame

# colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)

class Cursor:
	
	def __init__(self, screen, x, y):
		self.screen = screen
		self._x = x
		self._y = y
		self.counter = 0
		self.is_clicked = False
		self.wait = False
		self.timer = 0
		self.visible = True

	def update(self, mouse_pos, z, selected_button):
		self.mouse_pos = mouse_pos
		self.selected_button = selected_button
		#self.blink()				

	def blink(self):

		if self.wait == True:
			self.timer +=1
			if self.timer == 10:
				self.timer = 0
				self.wait = False	
		if self.counter <= 5:
			self.visible = False
			self.counter +=1
		elif self.counter <= 10:
			self.visible == True
			self.counter += 1
		else:
			self.counter = 0

	def set_x(self, x):
		self._x = x

	def set_y(self, y):
		self._y = y	

	def draw(self, mouse_pos):
		
		if self.visible == True:
			self.screen.fill(black, rect = ((self._x, self._y), (2, 15)))