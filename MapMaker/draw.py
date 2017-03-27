import pygame

# colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)


class Draw:

	def __init__(self, screen, displayWidth, displayHeight, font, handler):
		self.screen = screen
		self.displayWidth = displayWidth
		self.displayHeight = displayHeight
		self.font = font
		self.handler = handler
		self.obj_list = self.handler.get_obj_list()

		# init Background color
		self.screen.fill(white)

	def message_to_screen(self, msg, x, y):
		screen_text = self.font.render(msg, True, black)
		self.screen.blit(screen_text, [x,y])	

	def draw(self, mouse_pos):
		'this is the main draw method. call every draw method here'

		# Background color
		self.screen.fill(white)	

		self.handler.draw()



	
