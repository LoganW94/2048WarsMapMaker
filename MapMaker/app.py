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
yellow = (255,255,0)
violet = (160,10,226)
orange = (255,165,0)

class App:
	'this class handles the app design'
	def __init__(self, handler):

		self.handler = handler
		
		"variables"  
		displayWidth = 800
		displayHeight = 600
		self.current_state = 0

		##########################################################################################
		"design app here"

		self.map_location = None
		self.current_map = None
		self.left_menu_x = 50
		self.left_menu_y = 50
		self.default_height = 20
		self.lngth = 150
		self.txtbx_y = self.lngth + 30
		self.txt_length = 60

		self.description = None
		self.mapsize = None
		self.playerone = "default"
		self.playertwo = "default"
		self.playerthree = "default"
		self.playerfour = "default"
		self.grid = []

		self.font = pygame.font.SysFont(None, 25)

		"define display"
		display = screen.Screen(displayWidth, displayHeight, white)
		self.display = display.get_screen()

		"init objects"
		self.mouse_cursor = cursor.Cursor(self.display)
		self.mouse_pointer = pointer.Pointer(displayWidth/2, displayHeight/2, self.display, black)

		"Start menu state"
		state_0 = 0

		_new_button = button.Button(self.display, "New Map", self.left_menu_x, self.left_menu_y, self.default_height, 80, self.font, grey, state_0, self.new_map_state)

		_load_button =  button.Button(self.display, "Load Map", self.left_menu_x, self.left_menu_y + 30, self.default_height, 85, self.font, grey, state_0, self.load_state)

		"don't touch these, just add relevent instances. Leave empty brackets if list not needed"
		self.tile_arr =[[]] 
		self.obj_list = [self.mouse_pointer, self.mouse_cursor]
		self.button_list = [_new_button, _load_button]
		##########################################################################################		
		self.handler.set_screen(self.display, displayWidth, displayHeight)
		self.set_lists_handler()


	
	def get_current_state(self):
		return(self.current_state)

	def set_current_state(self, current_state):
		self.current_state = current_state

	###############################################################################################
	'Add app specific methods here'

	def update(self):
		self.set_lists_handler()

	def new_map_state(self):
		self.set_current_state(1)
		self.mouse_cursor.set_default()

		state_1 = 1
	
		_text_description = button.Display_Box(self.display, "Map Description", self.left_menu_x, self.left_menu_y, self.default_height, self.lngth, self.font, white, state_1)
		_description = button.Text_Box(self.display, self.left_menu_x +self.txtbx_y, self.left_menu_y, self.default_height, 200, self.font, state_1, self.mouse_cursor, self.handler)

		_text_mapsize = button.Display_Box(self.display, "Map Size", self.left_menu_x, self.left_menu_y +30, self.default_height, self.lngth, self.font, white, state_1)
		_mapsize = button.Text_Box(self.display, self.left_menu_x +self.txtbx_y, self.left_menu_y +30, self.default_height, 30, self.font, state_1, self.mouse_cursor, self.handler)

		_text_playerone = button.Display_Box(self.display, "Player Name", self.left_menu_x, self.left_menu_y+60, self.default_height, self.lngth, self.font, white, state_1)
		_playerone = button.Text_Box(self.display, self.left_menu_x +self.txtbx_y, self.left_menu_y+60, self.default_height, 75, self.font, state_1, self.mouse_cursor, self.handler)

		_text_playertwo = button.Display_Box(self.display, "NPC One", self.left_menu_x, self.left_menu_y+90, self.default_height, self.lngth, self.font, white, state_1)
		_playertwo = button.Text_Box(self.display, self.left_menu_x +self.txtbx_y, self.left_menu_y+90, self.default_height, 75, self.font, state_1, self.mouse_cursor, self.handler)

		_text_playerthree = button.Display_Box(self.display, "NPC Two", self.left_menu_x, self.left_menu_y+120, self.default_height, self.lngth, self.font, white, state_1)
		_playerthree = button.Text_Box(self.display, self.left_menu_x +self.txtbx_y, self.left_menu_y+120, self.default_height, 75, self.font, state_1, self.mouse_cursor, self.handler)

		_text_playerfour = button.Display_Box(self.display, "NPC Three", self.left_menu_x, self.left_menu_y+150, self.default_height, self.lngth, self.font, white, state_1)
		_playerfour = button.Text_Box(self.display, self.left_menu_x +self.txtbx_y, self.left_menu_y+150, self.default_height, 75, self.font, state_1, self.mouse_cursor, self.handler)

		_save_button = button.Button(self.display, "Generate Map Grid", self.left_menu_x, self.left_menu_y + 200, self.default_height, 150, self.font, grey, state_1, self.create_new_map)

		state_list = [_text_description, _description, _text_mapsize, 
		_mapsize, _text_playerone, _playerone, _text_playertwo, 
		_playertwo, _text_playerthree, _playerthree, 
		_text_playerfour, _playerfour, _save_button]	

		self.button_list = state_list

		self.set_lists_handler()

	def load_state(self):
		self.set_current_state(2)
		self.mouse_cursor.set_default()
		state_2 = 2

		_file_location_box = button.Text_Box(self.display, self.left_menu_x, self.left_menu_y, self.default_height, 200, self.font, state_2, self.mouse_cursor, self.handler)

		_load_map_button = button.Button(self.display, "Load map", self.left_menu_x, self.left_menu_y + 30, self.default_height, 100, self.font, grey, state_2, self.load_map)

		_print_map_button = button.Button(self.display, "print map to console", self.left_menu_x, self.left_menu_y + 60, self.default_height, 200, self.font, grey, state_2, self.print_map)

		state_list =[_file_location_box, _load_map_button, _print_map_button]

		self.button_list = state_list

		self.set_lists_handler()	

	def	mapmaker_state(self):
		self.set_current_state(3)
		self.mouse_cursor.set_default()	

		state_3 = 3
		

		_text_green = button.Display_Box(self.display, "tree", (self.left_menu_x + 20), self.left_menu_y, self.default_height, self.txt_length, self.font, white, state_3)
		_paint_green = button.Paint_Button(self.display, self.left_menu_x, self.left_menu_y, self.default_height, self.font, green, state_3, self.mouse_pointer)

		_text_grey = button.Display_Box(self.display, "rock", (self.left_menu_x + 20), self.left_menu_y+self.default_height, self.default_height, self.txt_length, self.font, white, state_3)
		_paint_grey = button.Paint_Button(self.display, self.left_menu_x, self.left_menu_y+self.default_height, self.default_height, self.font, grey, state_3, self.mouse_pointer)

		_text_white = button.Display_Box(self.display, "plains", (self.left_menu_x + 20), self.left_menu_y+(self.default_height*2), self.default_height, self.txt_length, self.font, white, state_3)
		_paint_white = button.Paint_Button(self.display, self.left_menu_x, self.left_menu_y+(self.default_height*2), self.default_height, self.font, white, state_3, self.mouse_pointer)

		_text_blue = button.Display_Box(self.display, "water", (self.left_menu_x + 20), self.left_menu_y+(self.default_height*3), self.default_height, self.txt_length, self.font, white, state_3)
		_paint_blue = button.Paint_Button(self.display, self.left_menu_x, self.left_menu_y+(self.default_height*3), self.default_height, self.font, blue, state_3, self.mouse_pointer)

		_text_orange = button.Display_Box(self.display, self.playerone, (self.left_menu_x + 20), self.left_menu_y+(self.default_height*4), self.default_height, self.txt_length, self.font, white, state_3)
		_paint_orange = button.Paint_Button(self.display, self.left_menu_x, self.left_menu_y+(self.default_height*4), self.default_height, self.font, orange, state_3, self.mouse_pointer)

		_text_yellow = button.Display_Box(self.display, self.playertwo, (self.left_menu_x + 20), self.left_menu_y+(self.default_height*5), self.default_height, self.txt_length, self.font, white, state_3)
		_paint_yellow = button.Paint_Button(self.display, self.left_menu_x, self.left_menu_y+(self.default_height*5), self.default_height, self.font, yellow, state_3, self.mouse_pointer)

		_text_red = button.Display_Box(self.display, self.playerthree, (self.left_menu_x + 20), self.left_menu_y+(self.default_height*6), self.default_height, self.txt_length, self.font, white, state_3)
		_paint_red = button.Paint_Button(self.display, self.left_menu_x, self.left_menu_y+(self.default_height*6), self.default_height, self.font, red, state_3, self.mouse_pointer)

		_text_violet = button.Display_Box(self.display, self.playerfour, (self.left_menu_x + 20), self.left_menu_y+(self.default_height*7), self.default_height, self.txt_length, self.font, white, state_3)
		_paint_violet = button.Paint_Button(self.display, self.left_menu_x, self.left_menu_y+(self.default_height*7), self.default_height, self.font, violet, state_3, self.mouse_pointer)

		_save_map_array = button.Button(self.display, "Save Map", self.left_menu_x, self.left_menu_y + (self.default_height * 10), self.default_height, 100, self.font, grey, state_3, self.save_map_array)

		state_list =[_text_orange, _paint_orange, _text_green, _paint_green, 
		_text_grey, _paint_grey, _text_white, _paint_white, _text_blue, 
		_paint_blue, _text_yellow, _paint_yellow, _text_red,
		 _paint_red, _text_violet, _paint_violet, _save_map_array]

		self.button_list = state_list

		self.set_lists_handler()

	def create_new_map(self):
		self.description = (self.button_list[1])._txt.title()
		self.mapsize = (self.button_list[3])._txt
		self.playerone = (self.button_list[5])._txt.title()
		self.playertwo = (self.button_list[7])._txt.title()
		self.playerthree = (self.button_list[9])._txt.title()
		self.playerfour = (self.button_list[11])._txt.title()

		self.map = newmap.New_Map(self.display, self.mouse_pointer, self.font, 
			self.description, self.mapsize, self.playerone, self.playertwo, self.playerthree, self.playerfour)
		self.mapmaker_state()
		self.tile_arr = self.map.get_grid()
		self.handler.set_lists(self.obj_list, self.button_list, self.tile_arr)

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


	def save_map_array(self):
		self.map.final_grid(self.tile_arr)

	def set_lists_handler(self):
		self.handler.set_lists(self.obj_list, self.button_list, self.tile_arr)	
		
