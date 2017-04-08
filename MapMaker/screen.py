import pygame

class Screen:

	def __init__(self, width, height, color):
		self.width = width
		self.height = height
		self.background_color = color

		pygame.init()

		self.screen = pygame.display.set_mode((self.width,self.height))

		pygame.display.set_caption('MapMaker Alpha')

		icon = pygame.image.load('assets/icon2.png')

		pygame.display.set_icon(icon)

		self.screen.fill(color)

	def get_screen(self):
		return self.screen
