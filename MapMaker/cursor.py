# colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)

class Cursor:
	
	def __init__(self, screen):
		self.screen = screen
		self.set_default()
		self.counter = 0
		self.is_clicked = False
		self.wait = False
		self.timer = 0
		self.visible = True

	def update(self, mouse_pos, z, selected_button):
		self.mouse_pos = mouse_pos
		self.selected_button = selected_button
		self.blink()				

	def blink(self):

		if self.wait == False:
			self.visible = False
			self.timer += 1
		elif self.wait == True:
			self.visible = True
			self.timer += 1		
		else:
			self.visible = True

		if self.timer == 10:
			self.wait = True
		elif self.timer == 20:
			self.wait = False
			self.timer = 0		

	def set_default(self):
		self._x = -10
		self._y = -10		

	def set_x(self, x):
		self._x = x

	def set_y(self, y):
		self._y = y	

	def draw(self, mouse_pos):
		
		if self.visible == True:
			self.screen.fill(black, rect = ((self._x, self._y), (1, 17)))