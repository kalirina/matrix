class vector():
	def __init__(self,data):
		if len(data) is 0:
			raise ValueError("Empty list in Vector initialisation")
		for el in data:
			if not isinstance(el,type(data[0])):
				raise ValueError("Elements in argument are not of same type")
		self.data = data

	def size(self):
		return len(self.data)

	def print(self):
		print(self.data)

	# ex00
	def add(self,v):
		self.data = [a + b for a, b in zip(self.data, v.data)]

	def sub(self,v):
		self.data = [a - b for a, b in zip(self.data, v.data)]

	def scl(self,a):
		self.data = [v * a for v in self.data]

	# ex01
	def linear_combination(u,coefs):
		res = 0
		for v in u:

		[el * coef for v in]


v = vector([2,4,23,5])
v1 = vector([254,47,23,5])

v1.sub(v)
v1.print()

v = vector()
