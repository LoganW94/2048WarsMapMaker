import pygame


class InputHandler:

	def __init__(self, screen, displayWidth, displayHeight):
		self._z = 0

		self.cursor_x = displayWidth/2
		self.cursor_y = displayHeight/2

		self.set_mouse_pos()

		self.screen = screen
		self.displayWidth = displayWidth
		self.displayHeight = displayHeight
		
		pygame.mouse.set_pos(self.mouse_pos)
		pygame.mouse.set_visible(False)

	def get_input(self):
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
	
# improper use of getter and setter. but it works for now
	def set_mouse_pos(self):
		self.mouse_pos = (self.cursor_x, self.cursor_y)			

	def get_mouse_pos(self):
		return self.mouse_pos

	def get_z(self):
		return self._z	