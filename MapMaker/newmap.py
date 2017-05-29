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

	def __init__(self, display, pointer, font):

		self.display = display
		self.pointer = pointer
		self.font = font

	def get_grid(self):
		return self.grid

	def new_map(self, description, mapsize, playerone, playertwo, playerthree, playerfour):

		self.mapsize = int(mapsize)
		self.description = description
		self.playerone = playerone
		self.playertwo = playertwo
		self.playerthree = playerthree
		self.playerfour = playerfour

		self.player_names = [self.playerone,self.playertwo,self.playerthree,self.playerfour]

		self.g = GameMap.new(self.mapsize)
		self.g.description = self.description
		self.g.player_names = self.player_names

		default_x = 200
		default_y = 50
		init_x = default_x
		default_size = 25

		row = []
		self.grid = []
		for x in range(self.mapsize):
			for y in range(self.mapsize):
				tile = button.Tile(self.display, default_x, default_y, default_size, self.font, white, 3, self.pointer)
				row.append(tile)
				default_x += default_size

			self.grid.append(row)
			row = []	
			default_y += default_size
			default_x = init_x	

	def loaded_map(self, json_in):

		self.g = GameMap.load(json_in)

		x = 0
		y = 0
		default_x = 200
		default_y = 50
		init_x = default_x
		default_size = 25
		
		row = []
		self.grid = []

		for x in range(self.g.get_map_size()):
			for y in range(self.g.get_map_size()):
				grid_item = self.g.get_grid_item(x,y)

				if(isinstance(grid_item,Terrain)):
					t_type = grid_item.terrtype
					if t_type == 'W' or t_type == 'w':
						color = blue
					if t_type == 'P' or t_type == 'p':
						color = white
					if t_type == 'R' or t_type == 'r':
						color = grey
					if t_type == 'T' or t_type == 't':
						color = green
					else:
						color = red	
					tile = button.Tile(self.display, default_x, default_y, default_size, self.font, color, 3, self.pointer)
					row.append(tile)
					default_x += default_size	
				self.grid.append(row)
				row = []	
			default_y += default_size
			default_x = init_x			


	def final_grid(self, grid, file_name):
		self.file_name = file_name

		x = 0
		y = 0

		self.grid = grid

		for i in self.grid:
			for r in i:
				
				if r.color == blue:
					self.g.put_terrain(x,y,'W')
				elif r.color == white:	
					self.g.put_terrain(x,y,'P')
				elif r.color == green:
					self.g.put_terrain(x,y,'T')
				elif r.color == grey:
					self.g.put_terrain(x,y,'R')
				elif r.color == orange:
					self.g.put_terrain(x,y,'P')
					self.g.put_city(x,y,0)	
				elif r.color == violet:
					self.g.put_terrain(x,y,'P')
					self.g.put_city(x,y,1)
				elif r.color == red:
					self.g.put_terrain(x,y,'P')
					self.g.put_city(x,y,2)
				elif r.color ==	yellow:
					self.g.put_terrain(x,y,'P')
					self.g.put_city(x,y,3)
				else:
					self.g.put_terrain(x,y,'P')				
				x+=1
			y+=1
			x=0		

		x=0
		y=0

		self.file_name = (self.file_name + ".json")
		f1=open(self.file_name, 'w+')
		f1.write(self.g.to_json())
		f1.close()		

	