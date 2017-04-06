from button import Button
import cursor

class TextBox(Button):

	def __init__(self, screen, x, y, height, width, font, color, input_handler):
		self.input_handler = input_handler
		self.cursor = cursor.Cursor(screen, (x+2), (y+2))
		Button.__init__(self, screen, ' ', x, y, height, width, font, color, self.cursor.clicked)

	def update(self, mouse_pos, z):
		self.mouse_pos = mouse_pos

		self.cursor.update()

		self.check_collide()

		self.change_color(z)

		if self.pressed == True:
			self.cursor.draw


	def when_pressed(self, z, m):
		if self.colide == True and z == 1 and self.pressed == False:
			m()
			self.pressed = True
		elif z == 0 and self.pressed == True:
			self.pressed = False	


	def draw(self, mouse_pos):
		self.mouse_pos = mouse_pos

		self.screen.fill(self.color, rect = ((self._x, self._y), (self._width, self._height)))

	
