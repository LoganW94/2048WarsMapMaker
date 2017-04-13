import pygame
import screen
import handler
import button
import pointer
import cursor

# colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)

class App:
	'this class handles the apps design'
	def __init__(self, handler):
		
		# variables  
		displayWidth = 800
		displayHeight = 600
		menu_state = 0

		##########################################################################################
		"design app here"

		font = pygame.font.SysFont(None, 25)

		# define display
		display = screen.Screen(displayWidth, displayHeight, white)
		display = display.get_screen()

		#init objects
		mouse_cursor = cursor.Cursor(display, 0, 0)
		mouse_pointer = pointer.Pointer(displayWidth/2, displayHeight/2, display, black)

		printbutton = button.Button(display, 
			'Print', 
			(displayWidth/2-25), 
			(displayHeight/2+20), 
			20, 50, 
			font, grey, 
			self.print_temp)

		textbox = button.TextBox(display, 
			(displayWidth/2-100), 
			(displayHeight/2+50), 
			20, 200, font,
			grey, mouse_cursor, handler)

		redbutton = button.Paint_Button(display, 100, 100, 20, font, red, mouse_pointer)
		greenbutton = button.Paint_Button(display, 100, 121, 20, font, green, mouse_pointer)
		bluebutton = button.Paint_Button(display, 100, 142, 20, font, blue, mouse_pointer)

		tile1 = button.Tile(display, 200, 100, 20, font, white, mouse_pointer)
		tile2 = button.Tile(display, 200, 121, 20, font, white, mouse_pointer)
		tile3 = button.Tile(display, 200, 142, 20, font, white, mouse_pointer)

		##########################################################################################		

		tile_arr = [tile1, tile2, tile3]

		obj_list = [mouse_pointer, mouse_cursor]
		button_list = [printbutton, textbox, redbutton, greenbutton, bluebutton]	

		handler.set_lists(obj_list, button_list, tile_arr)
		handler.set_screen_size(display, displayWidth, displayHeight)

	def print_temp(self):
		print("print button")	