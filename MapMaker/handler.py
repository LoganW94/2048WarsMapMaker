import pygame

class Handler:
	
	def __init__(self, obj_list, button_list, input_handler):
		self._temp = 0
		self._obj_list = obj_list
		self.button_list = button_list
		self.selected_button = None
		self.input_handler = input_handler
		self.exclude = None

	def update(self, mouse_pos, menu_state, z):
		self.mouse_pos = mouse_pos
		#exclude = None

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

		print(self.exclude)

	def draw(self):

		for x in self.button_list:
			x.draw(self.mouse_pos)

		for i in self._obj_list:
			i.draw(self.mouse_pos)
	

	def get_obj_list(self):
		return self._obj_list	

	def get_mouse_pos(self):
		return self.mouse_pos