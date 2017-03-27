import pygame

pygame.init()

# colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)

font = pygame.font.SysFont(None, 25)

def message_to_screen(screen, msg, x, y):
	screen_text = font.render(msg, True, black)
	screen.blit(screen_text, [x,y])

class Draw:

	def __init__(self, screen):
		self.screen = screen

		# Background color
		self.screen.fill(white)		

	def draw_pointer(self, mouse_pos):
	# Mouse pointer
		self.screen.fill(black, rect = ((mouse_pos[0], mouse_pos[1]-5), (1, 11)))
		self.screen.fill(black, rect = ((mouse_pos[0]-5, mouse_pos[1]), (11, 1)))

	def draw_to_screen(self, mouse_pos):
		'this is the main draw method. call every draw method here'
		self.draw_pointer(mouse_pos)


