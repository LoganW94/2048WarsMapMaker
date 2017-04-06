from gamemap import GameMap
from griditem import *
import sys


# use GameMap.new to generate a new gamemap
g = GameMap.new(5)

# Show how to read terrain (it's all water)
print("Item type here is " + str((g.get_grid_item(0,0).terrtype)))
print("Item type here is " + str((g.get_grid_item(4,4).terrtype)))

# Show how to get player names
print("Player names are " + str(g.player_names))

# Show how to change player names
g.player_names = ["A","B","C","D"]
print("Player names are " + str(g.player_names))

# Show how to get map size (helpful when loading maps)
print("Map size is " + str(g.get_map_size()))

# Show how to place some land down
g.put_terrain(1,1,'P')
g.put_terrain(1,2,'P')
g.put_terrain(1,3,'P')

# Show how to put a unit down (automatically converts underlying terrain to plains)
g.put_settler(2,1,0)
g.put_warrior(2,2,0,1)
g.put_warrior(2,3,2,2)

# Put other terrain down
g.put_terrain(3,1,'W')
g.put_terrain(3,2,'R')
g.put_terrain(3,3,'T')

# Show how to identify a type (which will help for drawing)
for x in range(g.get_map_size()):
	for y in range(g.get_map_size()):
		grid_item = g.get_grid_item(x,y)
		if(isinstance(grid_item,Terrain)):
			sys.stdout.write(grid_item.terrtype)
		if(isinstance(grid_item,Settler)):
			sys.stdout.write('s')
		if(isinstance(grid_item,Warrior)):
			sys.stdout.write('w')
	print('')


# Show how to place a city. A city can coexist on any tile that is not a ROCK, TREE, or WATER.
g.put_city(1,1,0)
print("Put a city at " + str(g.get_cities()[0].x) + "," + str(g.get_cities()[0].y) + " which belongs to faction " + str(g.get_cities()[0].faction)) 

# Remove city
g.remove_city(1,1)
print("Now there are " + str(len(g.get_cities())) + " cities left")

# put it back but on the other side
g.put_city(1,3,0)
print("Put a city at " + str(g.get_cities()[0].x) + "," + str(g.get_cities()[0].y) + " which belongs to faction " + str(g.get_cities()[0].faction)) 


# How to save
# print ("map as JSON is " + g.to_json())
f1=open('testmap_out.json', 'w+')
f1.write(g.to_json())
f1.close()

print("file was saved")

# File was saved as testmap_out.json.

# Now -> open the file we just saved
with open('testmap_out.json', 'r') as f:
	json_in=f.read().replace('\n', '')

g = GameMap.load(json_in)
print("file was loaded")

# Prove loaded map was identical to saved map
for x in range(g.get_map_size()):
	for y in range(g.get_map_size()):
		grid_item = g.get_grid_item(x,y)
		if(isinstance(grid_item,Terrain)):
			sys.stdout.write(grid_item.terrtype)
		if(isinstance(grid_item,Settler)):
			sys.stdout.write('s')
		if(isinstance(grid_item,Warrior)):
			sys.stdout.write('w')
	print('')

print("There are " + str(len(g.get_cities())) + " cities")
