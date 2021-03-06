from math import __sqrt as __sqrt, __acos as __acos, degrees as __deg

class Vector:
	"""	Creates a Vector Object."""

	# Initialisation
	def __init__(self, x=0, y=0, z=0):
		self.__availDTypes = [int, float]

		if (type(x) in self.__availDTypes) and (type(y) in self.__availDTypes) and (type(z) in self.__availDTypes):
			self.__x = x
			self.__y = y
			self.__z = z
		else:
			raise TypeError("Unsupported Data Type; Should be either int or float")

	# Getters
	@property
	def x(self):
		return self.__x

	@property
	def y(self):
		return self.__y

	@property
	def z(self):
		return self.__z

	# Setters
	@x.setter
	def x(self, Int):
		if type(Int) in self.__availDTypes:
			self.__x = Int
		else:
			raise ValueError("Unsupported Data Type for Direction Ratio")

	@y.setter
	def y(self, Int):
		if type(Int) in self.__availDTypes:
			self.__y = Int
		else:
			raise ValueError("Unsupported Data Type for Direction Ratio")

	@z.setter
	def z(self, Int):
		if type(Int) in self.__availDTypes:
			self.__z = Int
		else:
			raise ValueError("Unsupported Data Type for Direction Ratio")

	# Arithmetic Operations
	def __add__(self, other):
		return Vector((self.x+other.__x),
					(self.y+other.__y),
					(self.z+other.__z))

	def __div__(self, scalar):
		if not isinstance(scalar, Vector):
			return Vector((self.x/scalar),
						(self.y/scalar),
						(self.z/scalar))
		else:
			raise TypeError("Unsupported operand type(s) for /")

	def __eq__(self, other):
		if isinstance(other, Vector):
			if self.directionRatios() == other.directionRatios():
				return True
			else:
				return False
		else:
			raise TypeError("Unsupported operand type(s) for ==")

	def __mul__(self, scalar):
		if not isinstance(scalar, Vector):
			return Vector(round((self.x*scalar), 2),
						round((self.y*scalar), 2),
						round((self.z*scalar), 2))
		else:
			raise TypeError("Unsupported operand type(s) for *")

	def __sub__(self, other):
		return Vector((self.x-other.__x),
					(self.y-other.__y),
					(self.z-other.__z))

	# Representation
	def __repr__(self):
		if (self.x < 0) or (self.y < 0) or (self.z < 0):
			str_res = "<Vector Object> with "

			if self.x < 0:
				str_res += f"({self.x})i + "
			else:
				str_res += f"{self.x}i + "

			if self.y < 0:
				str_res += f"({self.y})j + "
			else:
				str_res += f"{self.y}j + "

			if self.z < 0:
				str_res += f"({self.z})k"
			else:
				str_res += f"{self.z}k"

			return str_res
		else:
			return f"<Vector Object> with {self.x}i + {self.y}j + {self.z}k"

	# Cross and Dot Products
	def cross(self, other):
		if isinstance(other, Vector):
			__X = round(((self.y*other.__z)-(other.__y*self.z)), 2)
			__Y = round(((self.x*other.__z)-(other.__x*self.z)), 2)
			__Z = round(((self.x*other.__y)-(other.__x*self.y)), 2)
			return Vector(__X, __Y, __Z)
		else:
			raise TypeError("Unsupported operand type; Requires Vector Object")

	def dot(self, other):
		if isinstance(other, Vector):
			return round(((self.x*other.__x)+(self.y*other.__y)+(self.z*other.__z)),
						2)
		else:
			raise TypeError("Unsupported operand type; Requires Vector Object")

	# Direction Angles, Direction Ratios and Direction Cosines
	def directionAngles(self):
		__dcs = self.directionCosines()
		return (round(__deg(__acos(__dcs[0])), 2),
				round(__deg(__acos(__dcs[1])), 2),
				round(__deg(__acos(__dcs[2])), 2))

	def directionCosines(self):
		__mag__ = self.magnitude()
		return (round((self.x/__mag__), 2),
				round((self.y/__mag__), 2),
				round((self.z/__mag__), 2))

	def directionRatios(self):
		return (self.x, self.y, self.z)

	# Magnitude of a Vector
	def magnitude(self):
		return round(__sqrt(((self.x)**2) + ((self.y)**2) + (self.z**2)), 2)

	def makesAngleWith(self, other):
		if isinstance(other, Vector):
			__dp, __prodmag = self.dot(other), (self.magnitude()*other.magnitude())
			return round(__deg(__acos(round(__dp/__prodmag, 2))), 2)
		else:
			raise TypeError("Unsupported operand type; Requires Vector Object")

	# Projection of a Vector and Projection Vector
	def projectionOn(self, other):
		if isinstance(other, Vector):
			__UnitOther__ = other.toUnit()
			return self.dot(__UnitOther__)
		else:
			raise TypeError("Unsupported operand type; Requires Vector Object")

	def projectionVectorOn(self, other):
		if isinstance(other, Vector):
			__UnitOther__ = other.toUnit()
			__projection__ = self.projectionOn(other)
			return __UnitOther__ * __projection__
		else:
			raise TypeError("Unsupported operand type; Requires Vector Object")

	# Conversion to Unit Vector
	def toUnit(self):
		__mag__ = self.magnitude()
		return Vector(round((self.x/__mag__), 2),
					round((self.y/__mag__), 2),
					round((self.z/__mag__), 2))