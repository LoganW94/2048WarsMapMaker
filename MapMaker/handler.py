import pygame

# colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)

class Obj_Handler:
	
	def __init__(self, obj_list, button_list, input_handler):
		self._temp = 0
		self._obj_list = obj_list
		self.button_list = button_list
		self.selected_button = None
		self.input_handler = input_handler
		self.exclude = None

	def update(self, mouse_pos, menu_state, z):
		self.mouse_pos = mouse_pos

		for i in self._obj_list:
			i.update(self.mouse_pos, z, self.selected_button)

		for x in self.button_list:
			x.update(self.mouse_pos, z)
			if x.is_selected == True and x != self.selected_button:
				self.exclude = self.button_list.index(x)
				for y in self.button_list:
					if self.button_list.index(y) != self.exclude:
						y.is_selected = False

				self.selected_button = x

	def draw(self):

		for x in self.button_list:
			x.draw(self.mouse_pos)

		for i in self._obj_list:
			i.draw(self.mouse_pos)
	

	def get_obj_list(self):
		return self._obj_list	

	def get_mouse_pos(self):
		return self.mouse_pos


class Input_Handler:

	def __init__(self, screen, displayWidth, displayHeight, font):
		self._z = 0

		self.cursor_x = displayWidth/2
		self.cursor_y = displayHeight/2

		self.set_mouse_pos()

		self.screen = screen
		self.displayWidth = displayWidth
		self.displayHeight = displayHeight
		
		pygame.mouse.set_pos(self.mouse_pos)
		pygame.mouse.set_visible(False)

		self.font = font
		self.recieve_input = False

		self.word = ''

	def get_input(self, selected_button):
		self.selected_button = selected_button

		# get user input
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				# closes out pygame and python script
				pygame.quit()
				quit()
			elif event.type == pygame.MOUSEMOTION:
				self.mouse_pos = event.pos	
			elif event.type == pygame.MOUSEBUTTONDOWN:
				self._z = 1
			elif event.type == pygame.MOUSEBUTTONUP:
				self._z = 0
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.word += " "
				elif event.key == pygame.K_BACKSPACE:
					self.word = self.word[:-1]
				else:
					key = pygame.key.name(event.key)
					self.word += key		

	def erase(self):
		self.word = ''	

	def set_mouse_pos(self):
		self.mouse_pos = (self.cursor_x, self.cursor_y)			

	def get_mouse_pos(self):
		return self.mouse_pos

	def get_z(self):
		return self._z

	def get_text_input(self):							
		return self.word		