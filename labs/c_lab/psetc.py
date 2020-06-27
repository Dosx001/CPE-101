# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set XII
# Term:         Winter 2020
def reverse_string(chars, n):
	if len(chars) == abs(n):
		return ''
	return chars[n - 1] + reverse_string(chars, n - 1)


def is_palindrome(chars, n):
#	if n == len(chars) // 2:
#		return chars[n] == chars[-n - 1]
#	return chars[n] == chars[-n -1] * is_palindrome(chars, n + 1)
	if n == len(chars) // 2:
		return chars[n] == chars[-n -1]
	return is_palindrome(chars, n + 1) and chars[n] == chars[-n -1]


def find_max(ints, n):
	if len(ints) == 1:
		return ints[0]
	ints.remove(ints[n] if ints[n] < ints[n + 1]
		else ints[n + 1])
	return find_max(ints, n)


def mul(x, y):
	if x == 0 or y == 0:
		return 0
	elif x < y:
		x, y = y, x
	if y == 1:
		return x
	return x + mul(x, y - 1)


def exp(x, y):
	if y == 0:
		return 1
	if y == 1:
		return x
	return mul(x, exp(x, y -1))


def factorial(n):
	if n == 0:
		return 1
	if n == 1:
		return n
	return mul(n , factorial(n - 1))


def fibonacci(n, acc):
	if n == 1:
		return acc[-1]
	elif n == 0:
		return 0
	return fibonacci(n - 1, acc + (acc[-1] + acc[-2], ))


def binary_search(ints, n, start, end):
	if n == ints[start]:
		return start
	mid = (start + end) // 2
	if n == ints[mid]:
		return mid
	if end - start <= 2:
		return -1
	if ints[mid] <= n:
		start = mid
	else:
		end = mid
	return binary_search(ints, n, start, end)


class NestingDoll:
	def __init__(self, count):
		self.inner = None
		if 1 < count + 1:
			self.inner = NestingDoll(count - 1)
	def __eq__(self, other):
		cur = self
		curr = other
		try:
			while cur.inner != None or curr.inner != None:
				cur = cur.inner
				curr = curr.inner
			return True
		except AttributeError:
			return False
	def __repr__(self):
		doll = "8"
		cur = self
		while cur.inner != None:
			cur = cur.inner
			doll = "(" + doll + ")"
		return doll
