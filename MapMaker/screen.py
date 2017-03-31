import pygame

class Screen:

	screen = pygame.display.set_mode((500,500)) 

	def __init__(self, width, height, color):
		self.width = width
		self.height = height
		self.background_color = color

		pygame.init()

		screen = pygame.display.set_mode((self.width,self.height))

		pygame.display.set_caption('MapMaker Alpha')

		screen.fill(color)
