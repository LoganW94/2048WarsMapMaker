from button import Button
import cursor

class TextBox(Button):

	def __init__(self, screen, x, y, height, width, font, color, cursor, input_handler ):
		self.cursor = cursor
		self.input_handler = input_handler
		self.word = None
		self._txt = " "
		Button.__init__(self, screen, self._txt, x, y, height, width, font, (200,200,200))

	def update(self, mouse_pos, z):
		self.mouse_pos = mouse_pos

		self.check_collide()

		self.change_color(z)

		self.when_pressed(z)

		#print(self.is_selected)

		if self.is_selected == True:
			self._txt = self.input_handler.get_text_input()
			print(self._txt)

	def when_pressed(self, z):
		if self.colide == True and z == 1 and self.pressed == False:
			self.input_handler.erase()
			self.pressed = True	
			self.cursor.set_x(self._x+2)
			self.cursor.set_y(self._y+2)
			self.is_selected = True
		elif z == 0 and self.pressed == True:
			self.pressed = False

	
