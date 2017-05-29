import pygame

class Screen:

	@staticmethod
	def new(width, height, color, caption='', imagepath=None):

		screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption(caption)
		try:
			icon = pygame.image.load(imagepath)
			pygame.display.set_icon(icon)
		except:
			Screen.error_msg(screen, "no image")
		screen.fill(color)
		return screen


	def error_msg(_screen, _txt):

		_color = (255,0,0)
		_x = 5
		_y = 5
		_font = pygame.font.SysFont(None, 15)

		screen_text = _font.render(_txt, True, _color)
		_screen.blit(screen_text, [_x, _y])
		