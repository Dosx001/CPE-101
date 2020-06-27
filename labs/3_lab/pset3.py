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
    """Return True if rotated is a rotation of word and False otherwise.
    A string is rotated by moving its last character to the front of the
    string (or vice versa); this step may be performed multiple times and
    still be considered a rotation. Any other scrambling of the characters is not a rotation. """
	return (x in y + y)


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
    """Return a string that contains the name of a color resulting from
    "mixing" the two given strings, each of which contains the name of a
    primary color (red, yellow, or blue). If both strings contain the same color,
    simply return that color."""
	if True == ((a != 'blue') and (b != 'blue') and (a != b)):
		return 'orange'
	elif True == ((a != 'red') and (b != 'red') and (a != b)):
		return 'green'
	elif True == ((a != 'yellow') and (b != 'yellow') and (a != b)):
		return 'purple'
	else:
		return a


def find_discriminant(a, b, c):
    """Return the result of calculating the discriminant as part of the quadratic formula.
    (The discriminant is the portion of the formula inside the square root operation,
    not including the square root operation.) Return None if the discriminant is negative. """
	d = b ** 2 - 4 * a * c
	if d >= 0:
		return d
	else:
		return None


def solve_poly(a, b, c):
	"""Return the result of calculating the quadratic formula
    for only the + value of the ± operation. Return None if the discriminant is negative.
    This function must call find_discriminant instead of reproducing its logic. """
    d = find_discriminant(a, b, c)
	if d == None or 0 == 2 * a or d < 0:
		return None
	else:
		return (d ** .5 -b) / (2 * a)
