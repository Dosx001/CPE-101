# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set IX
# Term:         Winter 2020
import pset9

x = [1, 3, 7, 1, 9, 6, 4]
y = [5, 1, 6, 8, 4, 3, 6]
z = [7, 6, 5, 4, 3, 2, 1]

assert pset9.sort_ints(x, 'bubble') == [1, 1, 3, 4, 6, 7, 9]
assert pset9.sort_ints(y, 'selection') == [1, 3, 4, 5, 6, 6, 8]
assert pset9.sort_ints(z, 'insertion') == [1, 2, 3, 4, 5, 6, 7]

assert pset9.bubble_pass(x) == [1, 3, 1, 7, 6, 4, 9]
assert pset9.bubble_pass(y) == [1, 5, 6, 4, 3, 6, 8]
assert pset9.bubble_pass(z) == [6, 5, 4, 3, 2, 1, 7]

assert pset9.selection_pass(x, 1) == [1, 1, 7, 3, 9, 6, 4]
assert pset9.selection_pass(y, 0) == [1, 5, 6, 8, 4, 3, 6]
assert pset9.selection_pass(z, 0) == [1, 6, 5, 4, 3, 2, 7] 

assert pset9.insertion_pass(x, 1) == [1, 3, 7, 1, 9, 6, 4]
assert pset9.insertion_pass(y, 1) == [1, 5, 6, 8, 4, 3, 6]
assert pset9.insertion_pass(z, 1) == [6, 7, 5, 4, 3, 2, 1]

w = list(range(0, 100)) 
assert pset9.binary_search(w, 84) == 84
assert pset9.binary_search(w, 28) == 28
assert pset9.binary_search(w, 200) == -1
