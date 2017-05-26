import json
from griditem import *
class GameMap:
	# Feel free to read and rewrite player names. Just make sure they are string lists!
	player_names = []

	# Private variables: Don't use these, use the methods I provide
	_cities = []
	_grid = []
	# Turn index not used yet.
	_turn_index = 0
	_map_size = 0

	# init a blank map of water. Pass integer as map size.
	# Defaults four player names.
	@staticmethod
	def new(size):
		g = GameMap()
		g._map_size = size
		g.player_names = ["Katakeets","Humans","Orks","Robots"]
		g.description = "A Default Map Description."
		g._inst_grid()
		return g

	# load map from string extracted from JSON file.
	@staticmethod
	def load(json_string):
		g = GameMap()
		mjson = json.loads(json_string)
		g.player_names = mjson["players"]
		g._turn_index = mjson["turn_index"]
		g._map_size = mjson["map_size"]
		g._inst_grid()
		i = 0;
		for j in mjson["grid"]:
			g._grid[i // g._map_size][i % g._map_size] = GameMap._grid_item_convert(j);
			i+=1

		# Todo assumes all mapmaker cities are lvl4
		for city in mjson["cities"]:
			g._cities.append(City(city["x"],city["y"],city["faction"]))
		return g

	# Pass 'W', 'R', 'T', or 'P' to create water, rock, trees, or plains.
	def put_terrain(self,x,y,terrtype):
		valid_types = ['W','R','T','P']
		if terrtype not in valid_types:
			raise RuntimeError("Invalid Terrain type passed: " + terrtype)
		if(not self._in_bounds(x,y)):
			
			raise RuntimeError("Cannot place terrain out of bounds")
		self._grid[x][y] = Terrain(terrtype)

	def put_settler(self,x,y,faction):
		if faction >= len(self.player_names):
			raise RuntimeError("Invalid Faction Number")
		if(not self._in_bounds(x,y)):
			raise RuntimeError("Cannot place settler out of bounds")
		self._grid[x][y] = Settler(faction)

	# strength can be any number from 1 up to 10
	# This should be modifiable in the map maker somehow
	def put_warrior(self,x,y,faction, strength):
		if faction >= len(self.player_names):
			raise RuntimeError("Invalid Faction Number")
		if(not self._in_bounds(x,y)):
			raise RuntimeError("Cannot place warrior out of bounds")
		self._grid[x][y] = Warrior(faction,strength)

	def put_city(self,x,y,faction):
		# Make sure we're in bounds and the faction is good.
		if faction >= len(self.player_names):
			raise RuntimeError("Invalid Faction Number")
		if(not self._in_bounds(x,y)):
			raise RuntimeError("Cannot place warrior out of bounds")

		# Terraform if we have to
		if self._grid[x][y] is Terrain:
			self._grid[x][y] = Terrain('P')

		# Delete old city if there is one there.
		self.remove_city(x,y)

		# place new city.
		self._cities.append(City(x,y,faction))

	def remove_city(self,x,y):
		# Delete old city if there is one there.
		self._cities = [city for city in self._cities if not (x == city.x and y == city.y)]

	def get_cities(self):
		return tuple(self._cities)

	def get_grid_item(self,x,y):
		if not self._in_bounds(x,y):
			raise RuntimeError("Lookup out of bounds")
		return self._grid[x][y]

	def get_map_size(self):
		return self._map_size

	def to_json(self):
		mjson = {}
		mjson["description"] = self.description
		mjson["players"] = self.player_names
		mjson["turn_index"] = self._turn_index
		mjson["map_size"] = self._map_size
		grid = []
		for i in range(self._map_size):
			for j in range(self._map_size):
				grid.append(self._grid[i][j]._to_json())
		mjson["grid"] = grid

		cities = []
		for city in self._cities:
			jcity = {}
			jcity["x"] = city.x;
			jcity["y"] = city.y;
			jcity["faction"] = city.faction;
			jcity["strength"] = city.strength;
			cities.append(jcity)

		mjson["cities"] = cities
		mjson["max_scores"] = [0 for x in self.player_names]
		return json.dumps(mjson)


### PRIVATE METHODS

	def _in_bounds(self,x,y):
		return (x > -1 and y > -1 and x < self._map_size and y < self._map_size)

	def _inst_grid(self):
		self._grid = [[Terrain('W') for x in range(self._map_size)] for x in range(self._map_size)]

	@staticmethod
	def _grid_item_convert(gjson):
		t = gjson["type"]
		if(t == "terrain"):
		# cheap shortcut
			return Terrain(gjson["terrain"][0].upper())
		elif(t == "settler"):
			return Settler(gjson["faction"])
		else:
			return Warrior(gjson["strength"],gjson["faction"])