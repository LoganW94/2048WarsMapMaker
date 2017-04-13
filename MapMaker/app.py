import pygame
import screen
import handler
import button
import pointer
import cursor
import newmap

"app specific imports"
import loadmap

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
		self.current_state = 0

		##########################################################################################
		"design app here"

		self.map_location = None
		self.current_map = None

		font = pygame.font.SysFont(None, 25)

		"define display"
		display = screen.Screen(displayWidth, displayHeight, white)
		display = display.get_screen()

		"init objects"
		mouse_cursor = cursor.Cursor(display, -10, -10)
		mouse_pointer = pointer.Pointer(displayWidth/2, displayHeight/2, display, black)

		"current_state 0 objects"
		state_0 = 0

		new_button = button.Button(display, "New Map", 360, 280, 20, 80, font, grey, state_0, self.create_new_map)

		load_button =  button.Button(display, "Load Map", 360, 310, 20, 85, font, grey, state_0, self.load_state)

		'current_state 1 objects'
		state_1 = 1

		textbox = button.Text_Box(display, 200, 200, 20, 100, font, state_1, mouse_cursor, handler)

		print_button = button.Button(display, "print textbox", 200, 230, 20, 100, font, grey, state_1, self.print_temp)

		'current_state 2 objects'
		state_2 = 2

		file_location_box = button.Text_Box(display, 200, 200, 20, 200, font, state_2, mouse_cursor, handler)

		load_map_button = button.Button(display, "Load map", 200, 230, 20, 100, font, grey, state_2, self.load_map)

		print_map_button = button.Button(display, "print map to console", 200, 260, 20, 200, font, grey, state_2, self.print_map)


		"don't touch these, just add relevent instances. Leave empty brackets if list not needed"
		self.tile_arr = []
		self.obj_list = [mouse_pointer, mouse_cursor]
		self.button_list = [new_button, load_button, textbox, print_button, file_location_box, load_map_button, print_map_button]
		##########################################################################################		

		handler.set_lists(self.obj_list, self.button_list, self.tile_arr)
		handler.set_screen(display, displayWidth, displayHeight)

	
	def get_current_state(self):
		return(self.current_state)

	def set_current_state(self, current_state):
		self.current_state = current_state

	###############################################################################################
	'Add app specific methods here'

	def print_temp(self):
		i = self.button_list[2]
		print(i._txt)

	def load_state(self):
		self.set_current_state(2)

	def create_new_map(self):
		grid = newmap.New_Map()
		self.set_current_state(1)

	def load_map(self):
		i = self.button_list[4]
		self.map_location = i._txt
		loader = loadmap.Load_Map(self.map_location)
		try:
			self.current_map = loader.get_file()
		except:
			print('no file found @ %s' % self.map_location)

	def print_map(self):
		try:
			print(self.current_map)
		except:
			print('no map loaded')
				