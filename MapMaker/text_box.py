from button import Button
import cursor

class TextBox(Button):

	def __init__(self, screen, x, y, height, width, color, cursor ):
		self.cursor = cursor
		Button.__init__(self, screen, x, y, height, width, color)

	def update(self, mouse_pos, z):
		self.mouse_pos = mouse_pos

		self.check_collide()

		self.change_color(z)

		if self.pressed == True:
			self.cursor.set_x(self._width)
			self.cursor.set_y(self._height)
			self.cursor.draw()


	def when_pressed(self, z, m):
		if self.colide == True and z == 1 and self.pressed == False:
			self.pressed = True	


	def draw(self, mouse_pos):
		self.mouse_pos = mouse_pos

		self.screen.fill(self.color, rect = ((self._x, self._y), (self._width, self._height)))

	
