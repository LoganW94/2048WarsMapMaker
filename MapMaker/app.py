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

		self.description = None
		self.mapsize = None
		self.playerone = None
		self.playertwo = None
		self.playerthree = None
		self.playerfour = None
		self.grid = None

		self.font = pygame.font.SysFont(None, 25)

		"define display"
		display = screen.Screen(displayWidth, displayHeight, white)
		self.display = display.get_screen()

		"init objects"
		self.mouse_cursor = cursor.Cursor(self.display, -10, -10)
		self.mouse_pointer = pointer.Pointer(displayWidth/2, displayHeight/2, self.display, black)

		"Start menu state"
		state_0 = 0

		_new_button = button.Button(self.display, "New Map", left_menu_x, left_menu_y, default_height, 80, self.font, grey, state_0, self.new_map_state)

		_load_button =  button.Button(self.display, "Load Map", left_menu_x, left_menu_y + 30, default_height, 85, self.font, grey, state_0, self.load_state)

		'New map state'
		state_1 = 1
		lngth = 150

		txtbx_y = lngth + 30

		_text_description = button.Display_Box(self.display, "Map Description", left_menu_x, left_menu_y, default_height, lngth, self.font, white, state_1)
		_description = button.Text_Box(self.display, left_menu_x +txtbx_y, left_menu_y, default_height, 200, self.font, state_1, self.mouse_cursor, handler)

		_text_mapsize = button.Display_Box(self.display, "Map Size", left_menu_x, left_menu_y +30, default_height, lngth, self.font, white, state_1)
		_mapsize = button.Text_Box(self.display, left_menu_x +txtbx_y, left_menu_y +30, default_height, 30, self.font, state_1, self.mouse_cursor, handler)

		_text_playerone = button.Display_Box(self.display, "Player Name", left_menu_x, left_menu_y+60, default_height, lngth, self.font, white, state_1)
		_playerone = button.Text_Box(self.display, left_menu_x +txtbx_y, left_menu_y+60, default_height, 75, self.font, state_1, self.mouse_cursor, handler)

		_text_playertwo = button.Display_Box(self.display, "NPC One", left_menu_x, left_menu_y+90, default_height, lngth, self.font, white, state_1)
		_playertwo = button.Text_Box(self.display, left_menu_x +txtbx_y, left_menu_y+90, default_height, 75, self.font, state_1, self.mouse_cursor, handler)

		_text_playerthree = button.Display_Box(self.display, "NPC Two", left_menu_x, left_menu_y+120, default_height, lngth, self.font, white, state_1)
		_playerthree = button.Text_Box(self.display, left_menu_x +txtbx_y, left_menu_y+120, default_height, 75, self.font, state_1, self.mouse_cursor, handler)

		_text_playerfour = button.Display_Box(self.display, "NPC Three", left_menu_x, left_menu_y+150, default_height, lngth, self.font, white, state_1)
		_playerfour = button.Text_Box(self.display, left_menu_x +txtbx_y, left_menu_y+150, default_height, 75, self.font, state_1, self.mouse_cursor, handler)

		_save_button = button.Button(self.display, "Generate Map Grid", left_menu_x, left_menu_y + 200, default_height, 150, self.font, grey, state_1, self.create_new_map)

		'Load map state'
		state_2 = 2

		_file_location_box = button.Text_Box(self.display, left_menu_x, left_menu_y, default_height, 200, self.font, state_2, self.mouse_cursor, handler)

		_load_map_button = button.Button(self.display, "Load map", left_menu_x, left_menu_y + 30, default_height, 100, self.font, grey, state_2, self.load_map)

		_print_map_button = button.Button(self.display, "print map to console", left_menu_x, left_menu_y + 60, default_height, 200, self.font, grey, state_2, self.print_map)

		'Mapmaker state'
		state_3 = 3




		"don't touch these, just add relevent instances. Leave empty brackets if list not needed"
		self.tile_arr = self.grid
		self.obj_list = [self.mouse_pointer, self.mouse_cursor]
		self.button_list = [_new_button, _load_button, 
		_text_description, _description, _text_mapsize, _mapsize, _text_playerone, _playerone, _text_playertwo, _playertwo, _text_playerthree, _playerthree, _text_playerfour, _playerfour, _save_button, 
		_file_location_box, _load_map_button, _print_map_button]
		##########################################################################################		

		handler.set_lists(self.obj_list, self.button_list, self.tile_arr)
		handler.set_screen(self.display, displayWidth, displayHeight)

	
	def get_current_state(self):
		return(self.current_state)

	def set_current_state(self, current_state):
		self.current_state = current_state

	###############################################################################################
	'Add app specific methods here'

	def new_map_state(self):
		self.set_current_state(1)	

	def load_state(self):
		self.set_current_state(2)

	def	mapmaker_state(self):
		self.set_current_state(3)

	def create_new_map(self):
		self.description = (self.button_list[3])._txt
		self.mapsize = (self.button_list[5])._txt
		self.playerone = (self.button_list[7])._txt
		self.playertwo = (self.button_list[9])._txt
		self.playerthree = (self.button_list[11])._txt
		self.playerfour = (self.button_list[13])._txt

		self.map = newmap.New_Map(self.display, self.mouse_pointer, self.font, self.description, self.mapsize, self.playerone, self.playertwo, self.playerthree, self.playerfour)
		self.mapmaker_state()
		

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
				