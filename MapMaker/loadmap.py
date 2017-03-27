
test = 123

class LoadMap:
	"""Loads map from designated file"""

	def __init__(self):
		self.test = test

	def openFile(self, url):
		with open(url, "r") as f:
			text = f.read()
			f.close
		return text	


	def printFile(self, d):
		print(d)		