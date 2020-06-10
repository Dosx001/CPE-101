# Name:		Andres Rodriguez 
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Wordsearch
# Term:         Winter 2020


def main():	
	string = input()
	words = input() 
	size = int(len(string) ** .5)
	if size != 1:
		fix = size - 1
	else:
		fix = size
	table = ''
	n = 0
	for i in range(len(string)):
		table = table + string[i]
		n += 1
		if n == size:
			table = table + '\n'
			n = 0
	final = ''
	count = words.count(' ') + 1
	for i in range(count):
		word = parse_word(words, i)
#		print(word)
		final = final + FF(string, word, size)
		final = final + FD(string, word, size)
		final = final + FU(string, word, size, fix)
		final = final + UU(string, word, size)
		final = final + BD(string, word, size, fix)
		final = final + BU(string, word, size)
		final = final + DD(string, word, size)
		final = final + BB(string, word, size)
	return print(table + final)


def FF(string, word, size):
	final = ''
	if word in string:
		loc = string.find(word)
		final = f"\n{word:>{size}}: [FF] ({loc//size}, {loc%size})"
	return final


def FD(string, word, size):
	final = ''
	m = size - 1
	w = size
	M = 1
	W = (size - 1) * (size + 1)
	for n in range(size * 2 - 1):
		if n < size:
#			print('   '+str(n)+'a')
#			print(ms(string, m, w, size + 1))
			if word in ms(string, m, w, size + 1):
				loc = ms(string, m, w, size + 1).find(word)
				final = final + f"\n{word:>{size}}: [FD] ({((size-1)-n+loc*(size+1))//size}, {((size-1)-n+loc*(size+1))%size})"
			m -= 1
			w += size
		else:		
#			print('   '+str(n)+'b')
#			print(ms(string, size * M, W, size + 1))
			if word in ms(string, size * M, W, size + 1):
				loc = ms(string, size * M, W, size + 1).find(word)
				final = final + f"\n{word:>{size}}: [FD] ({(size*M+loc*(size+1))//size}, {(size*M+loc*(size+1))%size})"
			M += 1
			W -= 1
	return final


def FU(string, word, size, fix):
		final = ''
		m = size - 1
		u = 1	
		for n in range(size * 2 - 1):
			if n < size:
#				print(str(n)+'a')
#				print(RMS(string, n, size * n + 1, size - 1))
				if word in RMS(string, n, size * n + 1, fix): 
					loc = RMS(string, n, size * n + 1, fix).find(word)
					final = final + f"\n{word:>{size}}: [FU] ({(size*n-loc*(size-1))//size}, {(size*u-loc*(size-1))%size})"
			else:	
#				print(str(n)+'b')
#				print(RMS(string, n + m, size * (size - 1) + n, size - 1))	
				if word in RMS(string, n + m, size * (size - 1) + n, fix):
					loc = RMS(string, n + m, size * (size - 1) + n, fix).find(word)
					final = final + f"\n{word:>{size}}: [FU] ({size-1-loc}, {((size-1)*size+u-loc*(size-1))%size})"
				m += size - 1
				u += 1	
		return final


def UU(string, word, size):
	final = ''
	if word in transpose_string(reverse_string(string), size):
		loc = transpose_string(reverse_string(string), size).find(word)
		final = f"\n{word:>{size}}: [UU] ({size-1-loc%size}, {size-1-loc//size})"
	return final


def BD(string, word, size, fix):
	final = ''
	m = size - 1
	u = 1
	for n in range(size * 2 - 1):
		if n < size:
#			print(str(n)+'a')
#			print(ms(string, n, size * n + 1, size - 1))
			if word in ms(string, n, size * n + 1, fix):
#				print(n)
#				print(ms(string, n, size * n + 1, size - 1))
				loc = ms(string, n, size * n + 1, fix).find(word)
#				print(loc)
				final = final + f"\n{word:>{size}}: [BD] ({loc}, {(n+loc*(size-1))%size})"
		else:	
#			print(str(n)+'b')
#			print(ms(string, n + m, size * (size - 1) + n, size - 1))	
			if word in ms(string, n + m, size * (size - 1) + n, fix):
				loc = ms(string, n + m, size * (size - 1) + n, fix).find(word)
				final = final + f"\n{word:>{size}}: [BD] ({loc+u}, {(n+u*(size-1)+loc*(size-1))%size})"
			m += size - 1
			u += 1
	return final


def BU(string, word, size):
	final = ''
	m = size - 1
	w = m + 1
	M = 1
	W = (size - 1) * (size + 1)
	for n in range(size * 2 - 1):
		if n < size:
#			print('   '+str(n)+'a')
#			print(RMS(string, m, w, size + 1))
			if word in RMS(string, m, w, size + 1):
				loc = RMS(string, m, w, size + 1).find(word)
				final = final + f"\n{word:>{size}}: [BU] ({(n*(size+1)-loc*(size+1)+m)//size}, {(n*(size+1)-loc*(size+1)+m)%size})"
			m -= 1
			w += size
		else:	
#			print('   '+str(n)+'b')
#			print(RMS(string, size * M, W, size + 1))
			if word in RMS(string, size * M, W, size + 1):
				loc = RMS(string, size * M, W, size + 1).find(word)
				final = final + f"\n{word:>{size}}: [BU] ({(W-1-loc*(size+1))//size}, {(W-1-loc*(size+1))%size})"
			M += 1
			W -= 1
	return final


def DD(string, word, size):
	final = ''
	if word in transpose_string(string, size):
		loc = transpose_string(string, size).find(word)
		final = f"\n{word:>{size}}: [DD] ({loc%size}, {loc//size})"
	return final


def BB(string, word, size):
	final = ''
	if word in reverse_string(string):
		loc = reverse_string(string).find(word)
		final = final + f"\n{word:>{size}}: [BB] ({size-1-loc//size}, {size-1-loc%size})"
	return final


def reverse_string(x):
	word = ''
	for i in x:
		word = i + word
	return word 


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


def ms(x, a, b, n):
	y = ''
	if b <= len(x):
        	z = range(a, b, n)
	else:
		z = range(a, len(x), n)
	for i in z:
		y = y + x[i] 
	return y


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


def RMS(x, a, b, n):
	return reverse_string(ms(x, a, b, n))


if __name__ == '__main__':
	main()
