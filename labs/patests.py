# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set X
# Term:         Winter 2020
import pseta

#assert pseta.try_open('text.txt', 'b.txt') == ['hello\n']
#assert pseta.try_open('a.txt', 'text.txt') == ['hello\n']
#assert pseta.try_open('a.txt', 'b.txt') == []

assert pseta.count_zeros([0, 1]) == 1
assert pseta.count_zeros([0, 1, 0, 2]) == 2
assert pseta.count_zeros([0, 1, 0, 2, 0, 3]) == 3

assert pseta.try_isalnum('abc') == True
assert pseta.try_isalnum('a1b2') == True
assert pseta.try_isalnum('!$@#') == False

assert pseta.get_numeric_type(1) == 'int'
assert pseta.get_numeric_type(1.0) == 'float'
assert pseta.get_numeric_type(2) == 'int'

assert pseta.get_sequence_type('') == 'str'
assert pseta.get_sequence_type([]) == 'list'
assert pseta.get_sequence_type(()) == 'tuple'

assert pseta.are_same_type('', '') == True
assert pseta.are_same_type(None, []) == False
assert pseta.are_same_type('', None) == False
assert pseta.are_same_type(None, None) == True
