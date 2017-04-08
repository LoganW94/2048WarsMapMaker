import pygame

# colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)

class InputHandler:

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