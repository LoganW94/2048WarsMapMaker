

class LoadMap:
	"""Loads map from designated file"""

	def __init__(self, url):
		self.url = url
		self.open_file()

	def open_file(self):
		with open(self.url, "r") as f:
			self.text = f.read()
			f.close


	def print_file(self):
		print(self.text)

	def get_text(self):
		return self.text		