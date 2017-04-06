class Terrain:
	def __init__(self, terrtype):
		self.terrtype = terrtype

	def json_name(self):
		return {'W' : "water",'T' : "tree",'R' : "rock",'P' : "plains"}[self.terrtype]
		# tree, water, rock, plains
	def _to_json(self):
		return {"type": "terrain","terrain" : self.json_name()}

class Settler:
	faction = None
	def __init__(self, faction):
		self.faction = faction

	def _to_json(self):
		return {"type": "settler","faction" : self.faction}

class Warrior:
	faction = None
	strength = None

	def __init__(self, faction, strength):
		self.faction = faction
		self.strength = strength

	def _to_json(self):
		return {"type": "warrior","strength" : self.strength, "faction" : self.faction}

class City:
	faction = None
	# Pass the X, Y, and faction id.
	# Don't worry abour changing the strength... yet.
	def __init__(self,x,y,faction):
		self.x = x
		self.y = y
		self.faction = faction
		self.strength = 4





