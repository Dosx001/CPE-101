# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set VIII
# Term:         Winter 2020


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y 
	
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __repr__(self):
		return f'({self.x}, {self.y})'

	def distance(self, to):
		return ((self.x - to.x) ** 2 + (self.y - to.y) ** 2) ** .5

	def get_slope_intercept(self, other):
		slope = (self.y - other.y) / (self.x - other.x)	
		intercept = other.y - slope * other.x
		return (slope, intercept)


class Circle:
	def __init__(self, center, radius):
		self.center = center
		self.radius = radius

	def __eq__(self, other):
		return self.center == other.center and self.radius == other.radius

	def __repr__(self):
		return f'{self.radius}r @ ({self.center.x}, {self.center.y})'

	def overlaps(self, other):
		return self.center.distance(other.center) < self.radius + other.radius

	def bisects(self, line):
		return self.center.y == line.m * self.center.x + line.b
	
	
class Line:
	def __init__(self, p1, p2):
		self.m = p1.get_slope_intercept(p2)[0]
		self.b = p1.get_slope_intercept(p2)[1]

	def __eq__(self, other):
		return self.m == other.m and self.b == other.b

	def __repr__(self):
		if 0 < self.b:
			return f'y = {self.m}x + {self.b}'
		elif 0 == self.b:
			return f'y = {self.m}x'
		else:
			return f'y = {self.m}x - {abs(self.b)}'
	
	def to_parallel(self, point):
		b = point.y - self.m * point.x
		new_y = self.m + b
		return Line(point, Point(1, new_y))

	def to_perpendicular(self):
		return Line(Point(0, self.b), Point(self.m, self.b - 1))


def get_point_distances(x):
	return [x[i].distance(Point(0, 0)) for i in range(len(x))]


def get_circle_distances(x):
	return [x[i].center.distance(Point(0, 0)) for i in range(len(x))]


def are_in_first_quadrant(x):
	return [x[i] for i in range(len(x)) if 0 < x[i].x if 0 < x[i].y]


def overlaps_unit_circle(x):
	return [x[i] for i in range(len(x)) if Circle(Point(0, 0), 1).overlaps(x[i])]
