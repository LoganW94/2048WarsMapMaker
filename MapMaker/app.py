import pygame
import screen
import handler
import button
import pointer
import cursor
import newmap

"colors"
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)

class App:
	'this class handles the apps design'
	def __init__(self, handler):
		
		"variables"  
		displayWidth = 800
		displayHeight = 600
		self.menu_state = 0

		##########################################################################################
		"design app here"

		font = pygame.font.SysFont(None, 25)

		"define display"
		display = screen.Screen(displayWidth, displayHeight, white)
		display = display.get_screen()

		"init objects"
		mouse_cursor = cursor.Cursor(display, -10, -10)
		mouse_pointer = pointer.Pointer(displayWidth/2, displayHeight/2, display, black)

		"menu_state 0 objects"
		state_0 = 0

		new_button = button.Button(display, "New Map", 360, 280, 20, 80, font, grey, state_0, self.create_new_map)

		load_button =  button.Button(display, "Load Map", 360, 310, 20, 85, font, grey, state_0, self.load_temp)

		'menu_state 1 objects'
		state_1 = 1

		textbox = button.Text_Box(display, 200, 200, 20, 100, font, state_1, mouse_cursor, handler)

		print_button = button.Button(display, "Load Map", 360, 310, 20, 85, font, grey, state_1, self.print_temp)

		"don't touch these, just add relevent instances. Leave empty brackets if list not needed"
		tile_arr = []
		obj_list = [mouse_pointer, mouse_cursor]
		button_list = [new_button, load_button]
		##########################################################################################		

		handler.set_lists(obj_list, button_list, tile_arr)
		handler.set_screen(display, displayWidth, displayHeight)

	
	def get_menu_state(self):
		return(self.menu_state)

	def set_menu_state(self, menu_state):
		self.menu_state = menu_state

	###############################################################################################
	'Add app specific methods here'

	def print_temp(self):
		print("print button")

	def load_temp(self):
		print("load button")

	def create_new_map(self):
		grid = newmap.New_Map()
		self.set_menu_state(1)