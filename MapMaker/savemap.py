import json

class SaveMap:

	def __init__(self, inhandler):
		self._temp_location = 'assets/'
		self._temp_name = 'test.json'

	def save(self):
		data = inhandler.get_output_text()
		file_location = (self._temp_location + self._temp_name)

		with open(file_location, 'w') as f:
			json.dump(data, f)
			f.close

			