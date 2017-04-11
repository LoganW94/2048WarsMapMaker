from button import Button

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

		if self.is_selected == True:
			self._txt = self.input_handler.get_text_input()

	def when_pressed(self, z):
		if self.colide == True and z == 1 and self.pressed == False:
			self.input_handler.erase()
			self.pressed = True	
			self.cursor.set_x(self._x+2)
			self.cursor.set_y(self._y+2)
			self.is_selected = True
		elif z == 0 and self.pressed == True:
			self.pressed = False


class Paint_Button(Button):

	def __init__(self, screen, x, y, size, font, color, pointer):
		self.size = size
		self.color = color
		self.pointer = pointer
		Button.__init__(self, screen, " ", x, y, self.size, self.size, font, color)

	def	update(self, mouse_pos, z):
		self.mouse_pos = mouse_pos

		self.check_collide()

		self.when_pressed(z)

		self.change_color(z)

	def when_pressed(self, z):
		if self.colide == True and z == 1 and self.pressed == False:
			self.pressed = True	
			self.is_selected = True
			self.pointer.change_color(self.color)
		elif z == 0 and self.pressed == True:
			self.pressed = False


class Tile(Button):

	def __init__(self, screen, x, y, size, font, color, pointer):
		self.size = size
		self.default_color = color
		self.color = self.default_color
		self.pointer = pointer
		Button.__init__(self, screen, " ", x, y, self.size, self.size, font, color)	

	def update(self, mouse_pos, z):	
		self.mouse_pos = mouse_pos

		self.check_collide()

		self.when_pressed(z)

		self.change_color(z)

	def when_pressed(self, z):
		if self.colide == True and z == 1 and self.pressed == False:
			self.pressed = True	
			self.is_selected = True
			self.color = self.pointer.color
		elif z == 0 and self.pressed == True:
			self.pressed = False		
