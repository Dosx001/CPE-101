# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set XII
# Term:         Winter 2020
import psetc

assert psetc.reverse_string('abc', 0) == 'cba'
assert psetc.reverse_string('123', 0) == '321'
assert psetc.reverse_string('fedcba', 0) == 'abcdef'

assert psetc.is_palindrome('racecar', 0) == True
assert psetc.is_palindrome('madam', 0) == True
assert psetc.is_palindrome('one', 0) == False

assert psetc.find_max([1, 2, 3], 0) == 3
assert psetc.find_max([10, 2, 6, 100], 0) == 100
assert psetc.find_max([5, 5, 5], 0) == 5

assert psetc.mul(1, 2) == 2
assert psetc.mul(100000, 3) == 300000
assert psetc.mul(0, 100000) == 0

assert psetc.exp(1, 0) == 1
assert psetc.exp(3, 4) == 81
assert psetc.exp(5, 6) == 15625

assert psetc.factorial(0) == 1
assert psetc.factorial(4) == 24
assert psetc.factorial(7) == 5040

assert psetc.fibonacci(0, (0, 1)) == 0
assert psetc.fibonacci(1, (0, 1)) == 1
assert psetc.fibonacci(7, (0, 1)) == 13

x = [1, 4, 5, 6, 7, 8, 10, 13, 15, 17, 20]
assert psetc.binary_search(x, 8, 0, len(x)) == 5
assert psetc.binary_search(x, 13, 0, len(x)) == 7
assert psetc.binary_search(x, 9, 0, len(x)) == -1
assert psetc.binary_search(x, 1, 0, len(x)) == 0

x = psetc.NestingDoll(1)
y = psetc.NestingDoll(2)
z = psetc.NestingDoll(3)

x.inner.inner == None
y.inner.inner.inner == None
z.inner.inner != None

assert x != y
assert y != z
assert x == x

assert str(x) == "(8)"
assert str(y) == "((8))"
assert str(z) == "(((8)))"
