class matrix():
	def __init__(self,data=[]):
		self.data = data

	def size(self):
		size = 0
		for row in self.data:
			for col in row:
				size += col
		return size

	def print(self):
		for row in self.data:
			print(row)

	def add(self, mat2):
		
