import pygame
import loadmap
import draw
import inputhandler
import handler
import button
import pointer

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
screen = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('MapMaker Alpha')

#init objects
button_1 = button.Button(screen, 'test button', displayWidth/2, displayHeight/2, 20, 100, font, grey)
pointer = pointer.Pointer(displayWidth/2, displayHeight/2, screen)

#init classes
handler = handler.Handler(button_1, pointer)
draw_to = draw.Draw(screen, displayWidth, displayHeight, font, handler)
handle_input = inputhandler.InputHandler(screen,displayWidth,displayHeight)



clock = pygame.time.Clock()

def start():
	gameExit = False
	
	loader = loadmap.LoadMap(tempJson)
	#loader.print_file()

	while not gameExit:

	# user input
		handle_input.get_input()
		mouse_pos = handle_input.get_mouse_pos()
		z = handle_input.get_z()
		handler.update(mouse_pos, menu_state, z)

	#need to add logic here	
				
	# Draw to screen
		draw_to.draw(mouse_pos)	
	
	# Update screen
		pygame.display.update()
		clock.tick(FPS)

start()	