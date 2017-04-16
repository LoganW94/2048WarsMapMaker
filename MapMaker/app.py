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
		left_menu_x = 50
		left_menu_y = 50
		default_height = 20

		font = pygame.font.SysFont(None, 25)

		"define display"
		display = screen.Screen(displayWidth, displayHeight, white)
		display = display.get_screen()

		"init objects"
		mouse_cursor = cursor.Cursor(display, -10, -10)
		mouse_pointer = pointer.Pointer(displayWidth/2, displayHeight/2, display, black)

		"Start menu state"
		state_0 = 0

		_new_button = button.Button(display, "New Map", left_menu_x, left_menu_y, default_height, 80, font, grey, state_0, self.create_new_map)

		_load_button =  button.Button(display, "Load Map", left_menu_x, left_menu_y + 30, default_height, 85, font, grey, state_0, self.load_state)

		'New map state'
		state_1 = 1
		lngth = 150

		txtbx_y = lngth + 30

		_text_description = button.Display_Box(display, "Map Description", left_menu_x, left_menu_y, default_height, lngth, font, white, state_1)
		_description = button.Text_Box(display, left_menu_x +txtbx_y, left_menu_y, default_height, 200, font, state_1, mouse_cursor, handler)

		_text_mapsize = button.Display_Box(display, "Map Size", left_menu_x, left_menu_y +30, default_height, lngth, font, white, state_1)
		_mapsize = button.Text_Box(display, left_menu_x +txtbx_y, left_menu_y +30, default_height, 30, font, state_1, mouse_cursor, handler)

		_text_playerone = button.Display_Box(display, "Player Name", left_menu_x, left_menu_y+60, default_height, lngth, font, white, state_1)
		_playerone = button.Text_Box(display, left_menu_x +txtbx_y, left_menu_y+60, default_height, 75, font, state_1, mouse_cursor, handler)

		_text_playertwo = button.Display_Box(display, "NPC One", left_menu_x, left_menu_y+90, default_height, lngth, font, white, state_1)
		_playertwo = button.Text_Box(display, left_menu_x +txtbx_y, left_menu_y+90, default_height, 75, font, state_1, mouse_cursor, handler)

		_text_playerthree = button.Display_Box(display, "NPC Two", left_menu_x, left_menu_y+120, default_height, lngth, font, white, state_1)
		_playerthree = button.Text_Box(display, left_menu_x +txtbx_y, left_menu_y+120, default_height, 75, font, state_1, mouse_cursor, handler)

		_text_playerfour = button.Display_Box(display, "NPC Three", left_menu_x, left_menu_y+150, default_height, lngth, font, white, state_1)
		_playerfour = button.Text_Box(display, left_menu_x +txtbx_y, left_menu_y+150, default_height, 75, font, state_1, mouse_cursor, handler)

		_save_button = button.Button(display, "Generate Map Grid", left_menu_x, left_menu_y + 200, default_height, 150, font, grey, state_1, self.print_temp)

		'Load map state'
		state_2 = 2

		file_location_box = button.Text_Box(display, left_menu_x, left_menu_y, default_height, 200, font, state_2, mouse_cursor, handler)

		load_map_button = button.Button(display, "Load map", left_menu_x, left_menu_y + 30, default_height, 100, font, grey, state_2, self.load_map)

		print_map_button = button.Button(display, "print map to console", left_menu_x, left_menu_y + 60, default_height, 200, font, grey, state_2, self.print_map)


		"don't touch these, just add relevent instances. Leave empty brackets if list not needed"
		self.tile_arr = []
		self.obj_list = [mouse_pointer, mouse_cursor]
		self.button_list = [_new_button, _load_button, 
		_text_description, _description, _text_mapsize, _mapsize, _text_playerone, _playerone, _text_playertwo, _playertwo, _text_playerthree, _playerthree, _text_playerfour, _playerfour, _save_button, 
		file_location_box, load_map_button, print_map_button]
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
				