# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set IV
# Term:         Winter 2020
import pset6

assert pset6.poly_add([1, 2, 3], [1, 2, 3]) == [2, 4, 6]
assert pset6.poly_add([1, 2, 3], [1, 2, 3]) == [2, 4, 6]
assert pset6.poly_add([1, 2, 3], [1, 2, 3]) == [2, 4, 6]

assert pset6.poly_mul([5, 5, 5], [5, 5, 5]) == [25, 50, 75, 50, 25]
assert pset6.poly_mul([1, 5, 1], [3, -10, 15]) == [3, 5, -32, 65, 15]
assert pset6.poly_mul([1, 0, 5], [1, -19, 9]) == [1, -19, 14, -95, 45]

assert pset6.get_mode([1, 2, 2, 3, 4]) == 2
assert pset6.get_mode([1, 2, 1]) == 1
assert pset6.get_mode([0, 0]) == 0

assert pset6.index_of_smallest([5, 4, 3, 2, 1]) == 4
assert pset6.index_of_smallest([]) == -1
assert pset6.index_of_smallest([1, 2, 0, 4]) == 2

assert pset6.has_duplicates([1, 2, 3, 1]) == True
assert pset6.has_duplicates([1, 2, 3]) == False
assert pset6.has_duplicates([1, 1, 2, 4]) == True

assert pset6.products([[1, 2], [], [5, 5]]) == [2, 0, 25]
assert pset6.products([[1, 6, 5], [1], [5, 10]]) == [30, 1, 50]
assert pset6.products([[1, 1], [20, 1], [5, 1]]) == [1, 20, 5]

assert pset6.fibonacci(1) == [0]
assert pset6.fibonacci(2) == [0, 1]
assert pset6.fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

assert abs(pset6.geo_mean([1, 1, 2, 5, 25]) - 3.0171) < 1e-4
assert abs(pset6.geo_mean([1, 1, 2, 5, 25]) - 3.0171) < 1e-4
assert pset6.geo_mean([]) == 0

assert abs(pset6.harmonic_mean([1, 2, 3]) - 1.6364) < 1e-4
assert abs(pset6.harmonic_mean([1, 2, 3]) - 1.6364) < 1e-4
assert abs(pset6.harmonic_mean([1, 2, 0, 3]) - 1.6364) < 1e-4
assert pset6.harmonic_mean([0, 0, 0]) == 0

assert pset6.nest_lists(1) == []
assert pset6.nest_lists(2) == [[]]
assert pset6.nest_lists(3) == [[[]]]

assert pset6.solve_bool_exp(["not", "X", "or", "not", "Y"], (True, False)) == True 
assert pset6.solve_bool_exp(["not", "X", "or", "Y"], (True, True)) == True
assert pset6.solve_bool_exp(["X", "and", "Y"], (False, True)) == False
