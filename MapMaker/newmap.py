import button
from gamemap import GameMap
from griditem import *
import sys

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)
yellow = (255,255,0)
violet = (160,10,226)
orange = (255,165,0)

class New_Map:

	grid = []

	def __init__(self, display, pointer, font, description, mapsize, playerone, playertwo, playerthree, playerfour):

		self.mapsize = int(mapsize)
		self.description = description
		self.playerone = playerone
		self.playertwo = playertwo
		self.playerthree = playerthree
		self.playerfour = playerfour

		self.player_names = [self.playerone,self.playertwo,self.playerthree,self.playerfour]

		default_x = 200
		default_y = 50
		init_x = default_x
		default_size = 25

		row = []
		self.grid = []
		for x in range(self.mapsize):
			for y in range(self.mapsize):
				tile = button.Tile(display, default_x, default_y, default_size, font, (255,255,255), 3, pointer)
				row.append(tile)
				default_x += default_size

			self.grid.append(row)
			row = []	
			default_y += default_size
			default_x = init_x
	
	def get_grid(self):
		return self.grid

	def final_grid(self, grid, file_name):
		self.file_name = file_name

		g = GameMap.new(self.mapsize)
		g.description = self.description
		g.player_names = self.player_names
		x = 0
		y = 0

		self.grid = grid

		for i in self.grid:
			for r in i:
				
				if r.color == blue:
					g.put_terrain(x,y,'W')
				elif r.color == white:	
					g.put_terrain(x,y,'P')
				elif r.color == green:
					g.put_terrain(x,y,'T')
				elif r.color == grey:
					g.put_terrain(x,y,'R')
				elif r.color == orange:
					g.put_terrain(x,y,'P')
					g.put_city(x,y,0)	
				elif r.color == violet:
					g.put_terrain(x,y,'P')
					g.put_city(x,y,1)
				elif r.color == red:
					g.put_terrain(x,y,'P')
					g.put_city(x,y,2)
				elif r.color ==	yellow:
					g.put_terrain(x,y,'P')
					g.put_city(x,y,3)
				else:
					g.put_terrain(x,y,'P')				
				x+=1
			y+=1
			x=0		

		x=0
		y=0

		self.file_name = (self.file_name + ".json")
		f1=open(self.file_name, 'w+')
		f1.write(g.to_json())
		f1.close()		

	