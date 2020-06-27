# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set IX
# Term:         Winter 2020


def sort_ints(x, m):
	if m == 'bubble':
		for i in range(len(x) - 1):
			x = bubble_pass(x)
		return x
	elif m == 'selection':
		for i in range(len(x)):
			x = selection_pass(x, i)
		return x
	else:#if m == 'insertion_pass':
		for i in range(len(x)):
			x = insertion_pass(x, i)
		return x


def bubble_pass(y):
	x = list(y)
	for i in range(len(y) - 1):
		if x[i + 1] < x[i]:
			x[i], x[i + 1] = x[i + 1], x[i]
	return x


def selection_pass(y, n):
	x = list(y)
	m = n
	for i in range(n, len(x)):
		if x[i] < x[n]:
			n = i
	x[m], x[n] = x[n], x[m]
	return x 


def insertion_pass(y, n):
	x = y[:n]
	loc = 0
	for i in range(n, -1, -1):
		if y[n] <= y[i]:
			loc = i
	x.insert(loc, y[n])
	return x + y[n + 1:]


def binary_search(z, n):
	x = list(z)
	y = 0
	#while not len(x) == 1:
	while x[0] != n or x[-1] != n: 
		if x[0] == x[-1]:
			break
		Size = len(x) // 2
		if x[Size] <= n:
			y += Size
			x = x[Size:]
		else:
			x = x[:Size]
	if x[0] == n:
		return y
	else:
		return -1 	
