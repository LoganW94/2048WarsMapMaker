import pygame

# colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)

class Handler:
	
	def __init__(self):
		
		'init variable'
		self.selected_button = None
		self.exclude = None
		self._z = 0	
		self.recieve_input = False
		self.word = ''

	def set_lists(self, obj_list, button_list, tile_arr):
		self._obj_list = obj_list
		self.button_list = button_list
		self.tile_arr = tile_arr
		self.selected_button = None

	def set_screen(self, screen, displayWidth, displayHeight):
		self.screen = screen
		self.cursor_x = 10
		self.cursor_y = 10

		self.set_mouse_pos()

		self.displayWidth = displayWidth
		self.displayHeight = displayHeight
		
		pygame.mouse.set_pos(self.mouse_pos)
		pygame.mouse.set_visible(False)		

	def update(self, current_state):
		self.current_state = current_state
		self.get_input()

		for i in self._obj_list:
			i.update(self.mouse_pos, self._z, self.selected_button)

		for x in self.button_list:
			x.update(self.mouse_pos, self._z, self.current_state)
			try:
				if x.is_selected == True and x != self.selected_button:
					self.exclude = self.button_list.index(x)
					for y in self.button_list:
						if self.button_list.index(y) != self.exclude:
							y.is_selected = False			

					self.selected_button = x
			except:
				self.selected_button = None				

		for i in self.tile_arr:
			for x in i:
				x.update(self.mouse_pos, self._z, self.current_state)			

	def draw(self):
		self.screen.fill(white)

		for x in self.button_list:
			x.draw(self.current_state)

		for y in self.tile_arr:
			for x in y:
				x.draw(self.current_state)

		for i in self._obj_list:
			i.draw(self.mouse_pos)			

	def get_input(self):

		alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				"closes out pygame and python script"
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
					if key in alphabet:
						self.word += key
					else:
						print(key)			

	def erase(self):
		self.word = ''	

	def set_mouse_pos(self):
		self.mouse_pos = (self.cursor_x, self.cursor_y)			

	def get_text_input(self):							
		return self.word				