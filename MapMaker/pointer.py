
class Pointer:

	def __init__(self, start_x, start_y, screen, color):
		self.color = color
		self.mouse_pos = (start_x, start_y)
		self.screen = screen

	def change_color(self, color):
		self.color = color
			
	def update(self, mouse_pos, z, selected_button):
		self.mouse_pos = mouse_pos
		self._z = z	

	def draw(self, mouse_pos):
		# Mouse pointer
		self.screen.fill((0,0,0), rect = ((self.mouse_pos[0], self.mouse_pos[1]-5), (3, 12)))
		self.screen.fill((0,0,0), rect = ((self.mouse_pos[0]-5, self.mouse_pos[1]), (12, 3)))
		self.screen.fill(self.color, rect = ((self.mouse_pos[0], self.mouse_pos[1]-5), (1, 11)))
		self.screen.fill(self.color, rect = ((self.mouse_pos[0]-5, self.mouse_pos[1]), (11, 1)))
		

