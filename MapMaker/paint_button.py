from button import Button

class Paint_Button(Button):

	def __init__(self, screen, x, y, size, font, color, pointer):
		self.size = size
		#self._height = self.size
		#self._width = self.size
		self.color = color
		self.pointer = pointer
		Button.__init__(self, screen, " ", x, y, self.size, self.size, font, color)

	def	update(self, mouse_pos, z):
		self.mouse_pos = mouse_pos

		self.check_collide()

		self.when_pressed(z)

	def when_pressed(self, z):
		if self.colide == True and z == 1 and self.pressed == False:
			self.pressed = True	
			self.is_selected = True
			self.pointer.change_color(self.color)
		elif z == 0 and self.pressed == True:
			self.pressed = False