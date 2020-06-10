# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set III
# Term:         Winter 2020


def is_positive(x):
	return x > 0


def both_positive(x, y):
	return is_positive(x) and is_positive(y)


def is_triangle(a, b, c):
	x = a + b > c
	y = a + c > b
	z = c + b > a 
	return x and y and z

 
def is_isosceles_triangle(a, b, c):
	x = is_triangle(a, b, c)
	y = a == b or a == c or b == c
	return x and y 


def is_int(n):
	return not '.' in str(n)


def abs_val(n):
	return -n if 0 > n else n


def is_rotation(x, y):
	return (x in y + y)# and x != y + y# and not x in y and not y in x


def max_of_two(x, y):
	if x > y:
		return x
	else:
		return y  

	
def max_of_three(x, y, z):
	if x > y and x > z:
		return x
	elif y > z:
		return y
	else:
		return z


def mix_colors(a, b):
	if True == ((a != 'blue') and (b != 'blue') and (a != b)):
		return 'orange'
	elif True == ((a != 'red') and (b != 'red') and (a != b)):
		return 'green'
	elif True == ((a != 'yellow') and (b != 'yellow') and (a != b)):
		return 'purple'
	else:
		return a


def find_discriminant(a, b, c):
	d = b ** 2 - 4 * a * c
	if d >= 0:
		return d
	else:
		return None


def solve_poly(a, b, c):
	d = find_discriminant(a, b, c)
	if d == None or 0 == 2 * a or d < 0:
		return None
	else:
		return (d ** .5 -b) / (2 * a)
