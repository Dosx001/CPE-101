# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set IV
# Term:         Winter 2020

 
def poly_add(x, y):
	z = []
	for i in range(len(x)):
		z.append(x[i] + y[i])
	return z


def poly_mul(x, y):
	z = []
	i = 0
	for w in range(2 * len(x) - 1):
		a = 0
		for n in range(len(x)):
			for m in range(len(y)):
				if n + m == i:
					a = a + x[n] * y[m]
		i += 1
		z.append(a)
	return z


def get_mode(x):
	y = 0
	for i in x:
		z = x.count(i)
		if y < z:
			y = z
			a = i
	return a


def index_of_smallest(x):
	if len(x) == 0:
		return -1
	else:
		a = x[0]
		z = 0
		for i in range(len(x)):
			b = x[i]
			if b < a:
				a = b
				z = i
		return z


def has_duplicates(x):
	for i in x:
		if 0 < i and 1 < x.count(i):
			return True
	return False


def products(x):
	z = []
	for i in range(len(x)):
		y = 1
		if len(x[i]) == 0: 
			z.append(0)
		else:
			for n in x[i]:
				y *= n
			z.append(y)
	return z


def fibonacci(x):
	z = []
	for i in range(x):
		if i < 2:
			z.append(i)
			a = 0
			b = 1
		else:
			c = a + b
			z.append(c)
			a = b
			b = c
	return z


def geo_mean(x):
	y = 1
	if len(x) == 0:
		return 0
	else:
		for i in x:
			y *= i
		return y ** (1 / len(x))


def harmonic_mean(x):
	n = 0
	while n < len(x):
        	if x[n] <= 0:
            		x.remove(x[n])
            		n -= 1
        	n += 1
	y = 0
	for i in x:
       		y += 1 / i
	if y == 0:
		return 0
	else:
		return len(x) / y   


def nest_lists(x):
	for i in range(x):
		if i == 0:
			y = []
			z = []
		else:
			z = [y]
			y = z
	return z


def solve_bool_exp(x, y):
	a = y[0]
	b = y[1]
	i = 0
	while i < len(x):
		if x[i] == 'not' and i == 0:
			a = not y[0]
		if x[i] == 'not' and i != 0:
			b = not y[1]
		if x[i] == 'and' or x[i] == 'or':
			c = x[i]
		i += 1
	if c == 'and':
		z = a and b
	else:
		z = a or b
	return z
