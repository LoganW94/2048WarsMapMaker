import pygame
import handler
import app

pygame.init()

clock = pygame.time.Clock()
FPS = 60

handler = handler.Handler()
app = app.App(handler)

def start():
	#init classes

	gameExit = False

	while not gameExit:

		# user input
		handler.update()

		# Draw to screen		
		handler.draw()
	
		# Update screen
		pygame.display.update()
		clock.tick(FPS)

start()	