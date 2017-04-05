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
	
