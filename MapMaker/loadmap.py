import json

class Load_Map:
	"""Loads map from designated file"""

	def __init__(self, url):
		self.open_file(url)


	def open_file(self, url):
		
		url = url + ".json"
		print(url)
		try:
			with open(url, "r") as f:
				text = f.read()
				f.close
				self.parsed_file = json.loads(text)
		except:
			print('no such file')


	def get_file(self):
		try:
			return self.parsed_file
		except:
			print("can't retrieve file")
				