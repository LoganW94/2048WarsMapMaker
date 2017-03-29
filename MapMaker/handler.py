import pygame
import button





class Handler:
	
	def __init__(self, button1, pointer):
		self._temp = 0
		self._obj_list = [button1, pointer]

	def update(self, mouse_pos, menu_state, z):

		self.mouse_pos = mouse_pos
		self.menu_state = menu_state
		self._z = z

		for i in self._obj_list:
			i.update(self.mouse_pos, self._z)

	def draw(self):
		for i in self._obj_list:
			i.draw(self.mouse_pos)

	def get_obj_list(self):
		return self._obj_list	

	def get_mouse_pos(self):
		return self.mouse_pos