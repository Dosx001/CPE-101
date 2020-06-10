# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set X
# Term:         Winter 2020

def try_open(primary, secondary):
	try:
		fp = open(primary, 'r')
		return fp.readlines()
		fp.close()
	except FileNotFoundError:
		try:
			fp = open(secondary, 'r')
			return fp.readlines()
			fp.close()
		except FileNotFoundError:
			return []


def count_zeros(ints):
	n = 0
	m = 0
	while True:
		try:	
			1 / ints[n]
		except ZeroDivisionError:
			m += 1
		except IndexError:
			return m
		n += 1


def try_isalnum(chars):
	n = 0
	while True:
		try:
			int(chars[n], 36)
			n += 1
		except ValueError:
			return False
		except IndexError:
			return True


def get_numeric_type(number):
	try:
		int(str(number), 10)
		return 'int'
	except ValueError:
		return 'float'
	
		
def get_sequence_type(sequence):
	try:
		sequence + ''
		return 'str'
	except TypeError:
		try:
			sequence.insert(0, 0)
			return 'list'
		except AttributeError:
			return 'tuple'


def are_same_type(x, y):
	try:
		x + y
		return True
	except TypeError:
		if (x == None) & (y == None):
			return True
		else:
			return False
#		try:
#			[] = x
#			return False
#		except TypeError:
#			try:
#				[] = y
#				return False
#			except TypeError:
#				return True 
#	return True
