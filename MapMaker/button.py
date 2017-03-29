import pygame
import loadmap
import savemap
import newmap

class Button:

	def __init__(self, screen, txt, x, y, height, width, font, color, method):
		self.screen = screen
		self._txt = txt
		self._x = x
		self._y = y
		self._height = height
		self._width = width
		self._font = font
		self.color = color
		self.method = method
		self.color_init = self.color
		r = self.color[0]
		g = self.color[1] 
		b = self.color[2] 
		r-=20
		g-=20
		b-=20
		self.new_color = (r,g,b)
		self.clicked_color = (r-10,g-10,b-10)
		self.colide = False
		self.pressed = False

	def update(self, mouse_pos, z):
		self.mouse_pos = mouse_pos

		self.check_collide()

		self.change_color(z)
		m = self.method
		self.when_pressed(z,m)

	def check_collide(self):
		mx = self.mouse_pos[0]
		my = self.mouse_pos[1]

		if mx >= self._x and mx <= (self._x + self._width) and my >= self._y and my <= (self._y + self._height):
			self.colide = True
		else:
			self.colide = False	

	def test(self):
		print(test)		

	def when_pressed(self, z, m):
		if self.colide == True and z == 1 and self.pressed == False:
			m()
			self.pressed = True
		elif z == 0 and self.pressed == True:
			self.pressed = False		
			
	def change_color(self, z):
		
		if self.colide == True and z == 1:
			self.color = self.clicked_color
		elif self.colide == True:
			self.color = self.new_color
		else:
			self.color = self.color_init	

	def draw(self, mouse_pos):
		self.mouse_pos = mouse_pos

		self.screen.fill(self.color, rect = ((self._x, self._y), (self._width, self._height)))
		screen_text = self._font.render(self._txt, True, (0,0,0))
		self.screen.blit(screen_text, [self._x +4, self._y+2])
