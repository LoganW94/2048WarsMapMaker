import pygame
import handler
import app

pygame.init()

clock = pygame.time.Clock()
FPS = 60

handler = handler.Handler()
app = app.App(handler)

def start():

	gameExit = False

	while not gameExit:

		handler.update(app.get_current_state())
		
		handler.draw()

		pygame.display.update()
		clock.tick(FPS)

start()	