import pygame
import screen
import loadmap
import handler
import button
import pointer
import cursor

pygame.init()

# colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)

#assets
icon = 'assets/icon.png'
tempJson = 'assets/turtle_island.json'

# variables  
displayWidth = 800
displayHeight = 600
FPS = 60
menu_state = 0

font = pygame.font.SysFont(None, 25)

# define display
screen = screen.Screen(displayWidth, displayHeight, white)
screen = screen.get_screen()

#init methods
loader = loadmap.LoadMap(tempJson)
handle_input = handler.Input_Handler(screen,
	displayWidth, 
	displayHeight, 
	font)

def display_message(message, x, y):
	screen_text = font.render(message, True, (0,0,0))
	screen.blit(screen_text, (x,y))

#init objects
cursor = cursor.Cursor(screen, 0, 0)
pointer = pointer.Pointer(displayWidth/2, displayHeight/2, screen, black)

loadbutton = button.Button(screen, 
	'Load', 
	(displayWidth/2-25), 
	(displayHeight/2-10), 
	20, 50, 
	font, grey, 
	loader.open_file)

printbutton = button.Button(screen, 
	'Print', 
	(displayWidth/2-25), 
	(displayHeight/2+20), 
	20, 50, 
	font, grey, 
	loader.print_file)

textbox = button.TextBox(screen, 
	(displayWidth/2-100), 
	(displayHeight/2+50), 
	20, 200, font,
	grey, cursor, handle_input)

textbox2 = button.TextBox(screen, 
	(displayWidth/2-100), 
	(displayHeight/2+80), 
	20, 200, font,
	grey, cursor, handle_input)

redbutton = button.Paint_Button(screen, 100, 100, 20, font, red, pointer)
greenbutton = button.Paint_Button(screen, 100, 121, 20, font, green, pointer)
bluebutton = button.Paint_Button(screen, 100, 142, 20, font, blue, pointer)

tile1 = button.Tile(screen, 200, 100, 20, font, white, pointer)
tile2 = button.Tile(screen, 200, 121, 20, font, white, pointer)
tile3 = button.Tile(screen, 200, 142, 20, font, white, pointer)

tile_arr = []

obj_list = [pointer, cursor]
button_list = [loadbutton, printbutton, textbox, textbox2, redbutton, greenbutton, bluebutton, tile1, tile2, tile3]

#init classes
handler = handler.Obj_Handler(obj_list, button_list, handle_input)

clock = pygame.time.Clock()

def start():
	gameExit = False

	while not gameExit:

		# user input
		handle_input.get_input(handler.selected_button)
		mouse_pos = handle_input.get_mouse_pos() 
		handler.update(mouse_pos, menu_state, z = handle_input.get_z())

		# Draw to screen

		display_message("this is a test", 100, 90)
		#draw_to.draw(mouse_pos)	
		screen.fill(white)	
		handler.draw()
	
		# Update screen
		pygame.display.update()
		clock.tick(FPS)

start()	