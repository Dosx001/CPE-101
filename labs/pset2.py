# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set II
# Term:         Winter 2020


def print_hello(name): 
	print('Hello', str(name))


def get_numbers():
	x = int(input('Pick a number: '))
	y = int(input('Pick another number: '))
	return x + y


def cube(x):
	return int(x) ** 3


def do_math(x, y):
	return (3 * int(x) ** 2 + 4 * int(y)) / (2 * int(x))


def get_hypotenuse(a, b):
	return (int(a) ** 2 + int(b) ** 2) ** .5


def get_distance(x1, y1, x2, y2):
	return get_hypotenuse(int(x2) - int(x1), int(y2) - int(y1))


def get_perimeter(x1, y1, x2, y2, x3, y3):
	a = get_distance(int(x1), int(y1), int(x2), int(y2))
	b = get_distance(int(x2), int(y2), int(x3), int(y3))
	c = get_distance(int(x3), int(y3), int(x1), int(y1))
	return a + b + c


def round_to_hundredths(x):
	Wh_Num = float(x) // 1
	Scrap = float(x) * 1000
	Dec = (Scrap - Wh_Num * 1000) // 1 
	Ten = Dec // 100
	Num = Dec - Ten * 100
	Hun = Num // 10
	Num = Num - Hun * 10
	Rounder = Num // 5
	print(((Wh_Num * 100) + (Ten * 10) + ((Hun + Rounder) * 1)) / 100)
	print(' ')
	return ((Wh_Num * 100) + (Ten * 10) + ((Hun + Rounder) * 1)) / 100






