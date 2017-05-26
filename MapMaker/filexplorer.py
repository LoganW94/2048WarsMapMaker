import os 
import subprocess
import pygame
from screen import Screen
from button import *
import cursor
import pointer
import handler

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

pygame.init()

clock = pygame.time.Clock()
FPS = 60

handler = handler.Handler()

class FileXplorer:

	def run(self):

		_width = 300
		_height = 250
		_tile_arr = []
		_button_list = []

		window = Screen.new(_width, _height, white)
		mouse_cursor = cursor.Cursor(window)
		mouse_pointer = pointer.Pointer(_width/2, _height/2, window, black)

		

		_obj_list = [mouse_pointer, mouse_cursor]

		handler.set_screen(window, _width, _height)

		handler.set_lists(_obj_list, _button_list, _tile_arr)

		while 1:

			handler.update(0)
			
			handler.draw()

			pygame.display.update()
			clock.tick(FPS)

