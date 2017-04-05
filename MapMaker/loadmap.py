import json

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

		self.parsed_file = json.loads(self.text)			

	def print_file(self):
		try:
			print(self.parsed_file)
		except:
			print('no file loaded')
		

	def get_text(self):
		try:
			return self.text
		except:
			print('no file loaded')
				