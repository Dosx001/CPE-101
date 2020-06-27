# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set IV
# Term:         Winter 2020


def all_input():
    """Repeatedly prompt the user for input until no characters
    are entered for a particular iteration. Return the concatenation
    of all characters entered. Strings can be concatenated using the + operator.
    You may want to use the built-in len function in the condition of the while loop. """
    x = 'a'
	y = ''
	while len(x) != 0:
		x = input('type some characters: ')
		y = y + x
	return	y


def mul(x, y):
	Mul = 0
	n = 1
	while n <= y:
		Mul += x
		n += 1
	return Mul


def exp(x, y):
	Exp = x
	n = 1
	while n < y:
		Exp = mul(x, Exp)
		n += 1
	return Exp


def div(x, y):
	n = 0
	while y <= x:
		x -= y
		n += 1	
	return n


def mod(x, y):
	return x - div(x, y) * y	


def gcd(x, y):
	n = 0
	m = 1
	while m <= x or m <= y:
		a = (x / m) % 1
		b = (y / m) % 1
		if a == 0 and b == 0:
			n = m
		m += 1	
	return n 


def is_prime(x):
	n = 2
	b = True
	while n < x and b == True:
		a  = x / n
		n += 1
		if a % 1 == 0 or x == 2: 
			b = False
	if x == 1:
		b = False
	return b


def sum_ints(start, end, n):
	total = 0
	m = 0
	while end > start + m:
		start += m
		m = n
		total += start
	return total


def sum_mul_table(x):
	n = 1
	total = 0
	while n <= x:
		total = total + sum_ints(n, x * n, n) + x * n
		n += 1 
	return total


def rotate_string(w,n):
    m = -1
    M = 0
    new = ''
    while abs(m) <= n:
        a = w[m]
        new = a + new
        m -= 1
    if abs(m) < len(w):
        while abs(m) <= len(w):
            b = w[M]
            m -= 1
            M += 1
            new = new + b
    return new


def weave_strings(s1, s2):
	x = len(s1)
	y = len(s2)
	n = 0
	w = ''
	while n < x or n < y:
		if n < x:
			a = s1[n]
			w = w + a
		if n < y:
			b = s2[n]
			w = w + b
		n += 1
	return w


def to_pig_latin(w):
	if w[0] in 'AEIOU':
        	return w + 'YAY'
	else:
		n = 0
		while not w[0] in 'AEIOU' and n != len(w): 
			w = w[1:] + w[0]
			n += 1
		return w + 'AY'
