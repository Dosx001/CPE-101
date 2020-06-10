# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set VII
# Term:         Winter 2020


def get_reciprocals(x):
	return [1 / x[i] for i in range(len(x)) if x[i] != 0]


def get_parities(x):
	return [['even', 'odd'][x[i] % 2] for i in range(len(x))]


def swap_ints(x):
	return [x[i] if i == len(x) - 1 and i % 2 != 1
	else [x[i - len(x) + 1], x[i - 1]][i % 2]
	for i in range(len(x))]


def group(x, n):
	return [[x[i] for i in 
	range(ii * n, n * ii + len(x) % n if ii == len(x) // n else n * ii + n)]
	for ii in range(len(x) // n if len(x) % n == 0 else len(x) // n + 1)]


def sum_until(x):
	return [sum(x[:i + 1]) for i in range(len(x))]


def reverse_all(x):
	return [x[i][::-1] for i in range(len(x) - 1, -1, -1)]


def find_maxes(x):
	return [max([int(ii) for ii in x[i]])
	for i in range(len(x))]


def transpose(x):
	return [[x[i][ii] for i in range(len(x))]
	for ii in range(len(x[0]))]


def sum_matrix_at(x, y):
	return [sum(x[ii // len(x[0])][ii % len(x[0])] for ii in y[i])
	for i in range(len(y))]


def sum_columns(x):
	return [sum(x[i][ii] for i in range(len(x)))
	for ii in range(len(x[0]))]
