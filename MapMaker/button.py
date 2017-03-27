import pygame


class Button:

	def __init__(self, screen, txt, x, y, height, width, font, color):
		self.screen = screen
		self._txt = txt
		self._x = x
		self._y = y
		self._height = height
		self._width = width
		self._font = font
		self.color = color


	#def check_collide(self, mouse_pos):
			
	def change_color(self):
		color_init = self.color
		self.color[0] += 20
		self.color[0] += 20
		self.color[0] += 20

	#def when_pressed(self, color):

	def draw(self, mouse_pos):
		self.mouse_pos = mouse_pos

		self.screen.fill(self.color, rect = ((self._x, self._y), (self._width, self._height)))
		screen_text = self._font.render(self._txt, True, (0,0,0))
		self.screen.blit(screen_text, [self._x +4, self._y+2])




		