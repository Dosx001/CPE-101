# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set V
# Term:         Winter 2020


def reverse_string(x):
	word = ''
	for i in x:
		word = i + word
	return word 


def translate_string(x, old, new):
	word = ''
	for i in x:
		if i == old:
			word = word + new
		else:
			word = word + i	
	return word


def rotate_chars(x, n):
	y = ''
	for i in x:
		if i.isalpha():
			if ord(i) + n >= 90:
				z = ord(i) + n % 26
			else:
				z = ord(i) + n
			if not chr(z).isalpha():
					z = z - 26
			if i.isupper() and chr(z).islower():
				z = n - (ord('Z') - ord(i)) + ord('A') - 1
			y = y + chr(z)
		else:
			y = y + i
	return y


def encode_ascii(x):
	z = ''
	for i in x:
		y = ord(i)
		z = z + f"{y:03}"
	return z


def parse_word(word, n):
	m = -1
	new = ''
	for i in word:
		if i != ' ':
			new = new + i
			work = new
		else:
			m += 1
			new = ''
		if m == n:
			break
	return work
	

def swap_chars(x):
    n = 0
    m = 1
    y = ''
    if len(x) % 2 == 0:
        z = range(int((len(x) / 2)))
    else:
        z = range(int((len(x) - 1) / 2))
    for i in z:
        y = y + x[m] + x[n]
        n += 2
        m += 2
    if len(x) % 2 != 0:
        y = y + x[-1]
    return y


def is_palindrome(x):
	y = ''
	for i in x:
		y = i + y
	return x == y


def decode_ascii(x):
	num = ''
	final = ''
	n = 0
	for i in x:
		num = num + i
		n += 1
		if n == 3:
			n = 0
			final = final + chr(int(num))
			num = ''	
	return final


def make_substring(x, a, b, n):
	y = ''
	if b <= len(x):
        	z = range(a, b, n)
	else:
		z = range(a, len(x), n)
	for i in z:
		y = y + x[i] 
	return y	


def longest_substring(s1, s2):
	word = ''
	if len(s1) < len(s2):
		a = s1
		b = s2
		n = len(a)
	else: 
		a = s2
		b = s1
		n = len(a)
	for i in range(0, len(a)):
		for n in range(len(a), 0 , -1):
			check = make_substring(a, i, n, 1)
			if check in b and len(word) < len(check):
				word = check
	return word
			

def transpose_string(x, w):
	y = ''
	n = 0
	m = 0
	o = 0
	for i in x:
		y = y + x[n + m]
		m += w
		o += 1
		if o == len(x) / w:
			n += 1
			m = 0	
			o = 0
	return	y
