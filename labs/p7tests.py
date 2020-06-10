# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set VII
# Term:         Winter 2020
import pset7

x = list(range(3))
y = list(range(4))
z = list(range(5))

assert pset7.get_reciprocals(x) == [1, 1 / 2]
assert pset7.get_reciprocals(y) == [1, 1 / 2, 1 / 3]
assert pset7.get_reciprocals(z) == [1, 1 / 2, 1 / 3 , 1 / 4]

assert pset7.get_parities(x) == ['even', 'odd', 'even']
assert pset7.get_parities(y) == ['even', 'odd', 'even', 'odd']
assert pset7.get_parities(z) == ['even', 'odd', 'even', 'odd', 'even']

assert pset7.swap_ints(x) == [1, 0, 2]
assert pset7.swap_ints(y) == [1, 0, 3, 2]
assert pset7.swap_ints(z) == [1, 0, 3, 2, 4]

assert pset7.group(x, 2) == [[0, 1], [2]]
assert pset7.group(y, 2) == [[0, 1], [2, 3]]
assert pset7.group(z, 3) == [[0, 1, 2], [3, 4]]

assert pset7.sum_until(x) == [0, 1, 3]
assert pset7.sum_until(y) == [0, 1, 3, 6]
assert pset7.sum_until(z) == [0, 1, 3, 6, 10]

assert pset7.reverse_all([x]) == [[2, 1, 0]]
assert pset7.reverse_all([x, y]) == [[3, 2, 1, 0], [2, 1, 0]]
assert pset7.reverse_all([x, y, z]) == [[4, 3, 2, 1, 0],
					 [3, 2, 1, 0], [2, 1, 0]]

assert pset7.find_maxes([['1'], ['2', '10']]) == [1, 10]
assert pset7.find_maxes([['2', '5'], ['50', '25', '75']]) == [5, 75]
assert pset7.find_maxes([['1', '3', '2'], ['7', '5', '2']]) == [3, 7]

assert pset7.transpose([x, x, x]) == [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
assert pset7.transpose([y, y, y, y]) == [[0, 0, 0, 0], [1, 1, 1, 1],
					[2, 2, 2, 2], [3, 3, 3, 3]]
assert pset7.transpose([z, z, z, z, z]) == [[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]

assert pset7.sum_matrix_at([x, x, x], [[1, 5, 2]]) == [5]
assert pset7.sum_matrix_at([y, y, y], [[1, 7, 5, 2], [3, 2, 6]]) == [7, 7]
assert pset7.sum_matrix_at([z, z, z],
	 [[1, 5, 2], [7, 10], [7, 9, 10], [1, 14]]) == [3, 2, 6, 5]

assert pset7.sum_columns([x, x, x]) == [0, 3, 6]
assert pset7.sum_columns([y, y, y]) == [0, 3, 6, 9]
assert pset7.sum_columns([z, z, z]) == [0, 3, 6, 9, 12]
