import pygame
import screen
import loadmap
import inputhandler
import handler
import button
import pointer
import cursor
import text_box

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
handle_input = inputhandler.InputHandler(screen,
	displayWidth, 
	displayHeight, 
	font)

#init objects
cursor = cursor.Cursor(screen, 0, 0)

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

textbox = text_box.TextBox(screen, 
	(displayWidth/2-100), 
	(displayHeight/2+50), 
	20, 200, font,
	grey, cursor, handle_input)

textbox2 = text_box.TextBox(screen, 
	(displayWidth/2-100), 
	(displayHeight/2+80), 
	20, 200, font,
	grey, cursor, handle_input)

pointer = pointer.Pointer(displayWidth/2, displayHeight/2, screen)

obj_list = [pointer, cursor]
button_list = [loadbutton, printbutton, textbox, textbox2]

#init classes
handler = handler.Handler(obj_list, button_list, handle_input)

clock = pygame.time.Clock()

def start():
	gameExit = False

	while not gameExit:

		# user input
		handle_input.get_input(handler.selected_button)
		mouse_pos = handle_input.get_mouse_pos() 
		handler.update(mouse_pos, menu_state, z = handle_input.get_z())

		# Draw to screen
		#draw_to.draw(mouse_pos)	
		screen.fill(white)	
		handler.draw()
	
		# Update screen
		pygame.display.update()
		clock.tick(FPS)

start()	