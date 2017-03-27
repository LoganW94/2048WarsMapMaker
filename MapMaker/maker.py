import pygame
import loadmap
import draw
import inputhandler

pygame.init()

#assets
icon = 'assets/icon.png'
tempJson = 'assets/turtle_island.json'

# variables 
displayWidth = 800
displayHeight = 600
FPS = 60
menu_state = 0

# define display
screen = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('MapMaker Alpha')

#init classes
draw_to = draw.Draw(screen)
handle_input = inputhandler.InputHandler(screen,displayWidth,displayHeight)

clock = pygame.time.Clock()

def start():
	gameExit = False
	
	loader = loadmap.LoadMap()
	map_data = loader.openFile(tempJson)

	while not gameExit:

	# user input
		handle_input.get_input()
		mouse_pos = handle_input.get_mouse_pos()
				
	# Draw to display
		#draw_to.draw_to_screen(mouse_pos)	
		screen.fill((0,0,0), rect = ((mouse_pos[0], mouse_pos[1]-5), (1, 11)))
		screen.fill((0,0,0), rect = ((mouse_pos[0]-5, mouse_pos[1]), (11, 1)))

	# temp screen text
		#draw.message_to_screen(screen, "LOAD",displayWidth/2, displayHeight/2)	
		#draw.message_to_screen(screen, "NEW", displayWidth/2, displayHeight/2-25)	
		#draw.message_to_screen(screen, "QUIT",displayWidth/2, displayHeight/2-50)		


	# Update display
		pygame.display.update()
		clock.tick(FPS)

start()	