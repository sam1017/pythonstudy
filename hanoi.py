class hanoi_cylinder():
	"""docstring for hanoi_cylinder"""
	def __init__(self, name):
		self.name = name
		self.array = []

	def get_name(self):
		return self.name

	def get_array(self):
		return self.array

def hanoi(n, x, y, z):
	if n == 1:
		move(x, z)
	else:
	    hanoi(n-1, x, z, y)
	    move(x , z)
	    hanoi(n-1, y, x, z)	

def move(x, z):
	value = x.get_array().pop()
	print(x.get_name() + " move " + str(value) + " to " + z.get_name())
	z.get_array().append(value)

x = hanoi_cylinder("X")
y = hanoi_cylinder("Y")
z = hanoi_cylinder("Z")
n = 6
for value in range(1,n):
	x.get_array().append(n-value)

hanoi(n-1,x,y,z)