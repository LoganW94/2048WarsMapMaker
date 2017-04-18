import button

class New_Map:

	def __init__(self, display, pointer, font, description, mapsize, playerone, playertwo, playerthree, playerfour):

		mapsize = int(mapsize)
		default_x = 200
		default_y = 200
		default_size = 15

		grid = [[None] * mapsize] * mapsize

		for y in grid:
			for x in y:
				print("x",default_x)
				x = button.Tile(display, default_x, default_y, default_size, font, (255,255,255), 3, pointer) 
				default_x += default_size
			print("y", default_y)
			default_y += default_size	

		print(description, mapsize, playerone, playertwo, playerthree, playerfour, grid)
		