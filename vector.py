class vector:
	def __init__(self,x = 0,y = 0,z = 0):
		self.x = x
		self.y = y
		self.z = z
	def dot(self, other): # other = other vector (view vector)
		return self.x*other.x+self.y*other.y+self.z*other.z
	def cross(self, other): #other = other vector (triangle side)
		N = vector()
		N.x = self.y * other.z - self.z * other.y
		N.y = self.z * other.x - self.x * other.z
		N.z = self.x * other.y - self.y * other.x
		return N