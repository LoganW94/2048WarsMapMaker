import button

class New_Map:

	grid = []

	def __init__(self, display, pointer, font, description, mapsize, playerone, playertwo, playerthree, playerfour):

		mapsize = int(mapsize)

		default_x = 200
		default_y = 50
		init_x = default_x
		default_size = 25

		row = []
		self.grid = []
		for x in range(mapsize):
			for y in range(mapsize):
				tile = button.Tile(display, default_x, default_y, default_size, font, (255,255,255), 3, pointer)
				row.append(tile)
				default_x += default_size

			self.grid.append(row)	
			default_y += default_size
			default_x = init_x

		

	def get_grid(self):
		return self.grid	