import pygame

# colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)

class Pointer:

	def __init__(self, start_x, start_y, screen):

		self.mouse_pos = (start_x, start_y)
		self.screen = screen

	def update(self, mouse_pos):
		self.mouse_pos = mouse_pos	

	def draw(self, mouse_pos):

		# Mouse pointer
		self.screen.fill(black, rect = ((self.mouse_pos[0], self.mouse_pos[1]-5), (1, 11)))
		self.screen.fill(black, rect = ((self.mouse_pos[0]-5, self.mouse_pos[1]), (11, 1)))
			