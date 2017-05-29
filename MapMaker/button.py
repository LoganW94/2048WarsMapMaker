
def default():
	print("default")

"colors"
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)
yellow = (255,255,0)
violet = (160,10,226)
orange = (255,165,0)	

class Button:

	def __init__(self, screen, txt, x, y, height, width, font, color, active_state, method = default):
		self.screen = screen
		self._txt = txt
		self._x = x
		self._y = y
		self._height = height
		self._width = width
		self._font = font
		self.color = color
		self.active_state = active_state
		self.method = method

		self.selected_color = self.get_selected_color(self.color)
		self.button_clicked_color = self.get_selected_color(self.selected_color)
		self.color_init = self.color
		self.colide = False
		self.pressed = False
		self.is_selected = False
		self.outline_color = (0,0,0)
					

	def update(self, mouse_pos, z, current_state):
		self.mouse_pos = mouse_pos
		current_state = current_state

		if current_state == self.active_state:
		 
			self.check_collide()

			self.change_color(z)

			self.when_pressed(z)

	def check_collide(self):
		mx = self.mouse_pos[0]
		my = self.mouse_pos[1]

		if mx >= self._x and mx <= (self._x + self._width) and my >= self._y and my <= (self._y + self._height):
			self.colide = True
		else:
			self.colide = False	
		

	def when_pressed(self, z):
		if self.colide == True and z == 1 and self.pressed == False:
			self.method()
			self.pressed = True
			self.is_selected = True
		elif z == 0 and self.pressed == True:
			self.pressed = False

	def get_selected_color(self, color):
		val = 30
		r = color[0]
		g = color[1] 
		b = color[2]
		color_init = (r,g,b)

		if r <val or g < val or b < val:
			new_color = color_init
		else:
			r-=val
			g-=val
			b-=val
			new_color = (r,g,b)	
		return new_color						
	
	def change_color(self, z):

		if self.colide == True and z == 1:
			self.color = self.button_clicked_color
		elif self.colide == True:
			self.color = self.selected_color
		else:
			self.color = self.color_init	

	def draw(self, current_state):
		current_state = current_state

		if current_state == self.active_state:

			self.screen.fill(self.color, rect = ((self._x, self._y), (self._width, self._height)))
			screen_text = self._font.render(self._txt, True, (0,0,0))
			self.screen.blit(screen_text, [self._x +4, self._y+2])

			#black outline around boxes

			self.screen.fill(self.outline_color, rect = ((self._x, self._y), (1, self._height)))
			self.screen.fill(self.outline_color, rect = ((self._x, self._y), (self._width, 1)))
			self.screen.fill(self.outline_color, rect = ((self._x + self._width, self._y), (1, self._height)))
			self.screen.fill(self.outline_color, rect = ((self._x, self._y+ self._height), (self._width, 1)))


class Text_Box(Button):

	def __init__(self, screen, x, y, height, width, font, active_state, cursor, handler):
		self.cursor = cursor
		self.handler = handler
		self.word = None
		self._txt = " "
		self.active_state = active_state
		Button.__init__(self, screen, self._txt, x, y, height, width, font, (200,200,200), self.active_state)

	def update(self, mouse_pos, z, current_state):
		self.mouse_pos = mouse_pos
		current_state = current_state

		if current_state == self.active_state:

			self.check_collide()

			self.change_color(z)

			self.when_pressed(z)

		if self.is_selected == True:
			self._txt = self.handler.get_text_input()
			self.move_cursor()

	def when_pressed(self, z):
		if self.colide == True and z == 1 and self.pressed == False:
			self.handler.erase()
			self.pressed = True	
			self.cursor.set_x(self._x+2)
			self.cursor.set_y(self._y+2)
			self.is_selected = True
		elif z == 0 and self.pressed == True:
			self.pressed = False

	def get_text(self):
		return self._txt

	def move_cursor(self):
		txt_width = self._font.size(self._txt) 
		self.cursor.set_x(self._x+2+ (txt_width[0]+2))

class Paint_Button(Button):

	def __init__(self, screen, x, y, size, font, color, active_state, pointer):
		self.size = size
		self.color = color
		self.active_state = active_state
		self.pointer = pointer
		Button.__init__(self, screen, " ", x, y, self.size, self.size, font, color, self.active_state)

	def update(self, mouse_pos, z, current_state):
		self.mouse_pos = mouse_pos
		current_state = current_state

		if current_state == self.active_state:

			self.check_collide()

			self.when_pressed(z)

			self.change_color()

	def change_color(self):

		if self.is_selected == True:
			self.outline_color = grey
		else:
			self.outline_color = black				

	def when_pressed(self, z):
		if self.colide == True and z == 1 and self.pressed == False:
			self.pressed = True	
			self.is_selected = True
			self.pointer.change_color(self.color)
		elif z == 0 and self.pressed == True:
			self.pressed = False

class Tile(Button):

	def __init__(self, screen, x, y, size, font, color, active_state, pointer):
		self.size = size
		self.default_color = color
		self.color = self.default_color
		self.active_state = active_state
		self.pointer = pointer
		Button.__init__(self, screen, " ", x, y, self.size, self.size, font, color, self.active_state)	

	def update(self, mouse_pos, z, current_state):
		self.mouse_pos = mouse_pos
		current_state = current_state

		if current_state == self.active_state:

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

	def change_color(self, z):
		if self.colide == True and z == 1:
			self.color = self.pointer.color	

class Display_Box(Button):

	def __init__(self, screen, txt, x, y, height, width, font, color, active_state):
		self._txt = txt
		self.default_color = color
		self.color = self.default_color
		self.active_state = active_state
		Button.__init__(self, screen, self._txt, x, y, height, width, font, self.color, self.active_state)
		
	def update(self, mouse_pos, z, current_state):
		self.mouse_pos = mouse_pos
		current_state = current_state