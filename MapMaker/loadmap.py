

class LoadMap:
	"""Loads map from designated file"""

	def __init__(self, url):
		self.url = url


	def open_file(self):
		try:
			with open(self.url, "r") as f:
				self.text = f.read()
				f.close
		except:
			print('no such file')		

	def print_file(self):
		try:
			print(self.text)
		except:
			print('no file loaded')
		

	def get_text(self):
		try:
			return self.text
		except:
			print('no file loaded')
				