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
		self.input_text = ''

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
			elif event.type == pygame.KEYDOWN and self.recieve_input == True:		
				self.input_text += event.key
	
# improper use of getter and setter. but it works for now
	def set_mouse_pos(self):
		self.mouse_pos = (self.cursor_x, self.cursor_y)			

	def get_mouse_pos(self):
		return self.mouse_pos

	def get_z(self):
		return self._z

	def get_text_input(self, input_text):
		output_text = self.font.render(input_text, True, black)
		self.screen.blit(output_text, [200,20])
		print(output_text)
		return output_text

	def arm(self):
		self.recieve_input == True

	def dis_arm(self):
		self.recieve_input == False

	def temp(self):
		print("I do not think that means what you think it means")