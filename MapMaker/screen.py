import pygame

class Screen:

	def new(width, height, color):

		screen = pygame.display.set_mode((width, height))

		pygame.display.set_caption('MapMaker Alpha')

		icon = pygame.image.load('assets/icon2.png')

		pygame.display.set_icon(icon)

		screen.fill(color)

		return screen
