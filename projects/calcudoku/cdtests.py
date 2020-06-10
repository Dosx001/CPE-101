# Name:		Andres Rodriguez 
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Calcudoku
# Term:         Winter 2020
import calcudoku

assert calcudoku.parse_word('computer help not', 0) == 'computer'
assert calcudoku.parse_word('computer help not', 1) == 'help'
assert calcudoku.parse_word('computer help not', 2) == 'not'

assert calcudoku.has_duplicates([1, 2, 3, 1]) == True
assert calcudoku.has_duplicates([1, 2, 3]) == False
assert calcudoku.has_duplicates([1, 1, 2, 4]) == True

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert calcudoku.get_col(grid, 3, 0) == [1, 4, 7]
assert calcudoku.get_col(grid, 3, 1) == [2, 5, 8]
assert calcudoku.get_col(grid, 3, 2) == [3, 6, 9]

assert calcudoku.cage_sum([0, 2, 4], grid, 3) == 9
assert calcudoku.cage_sum([1, 2, 4], grid, 3) == 10
assert calcudoku.cage_sum([1, 5, 4], grid, 3) == 13

assert calcudoku.grid_size_finder(1, [[10, 3, 5, 2, 8]]) == 3
assert calcudoku.grid_size_finder(1, [[10, 3, 5, 2, 15]]) == 4
assert calcudoku.grid_size_finder(1, [[10, 35, 2, 8]]) == 6

assert calcudoku.display_grid(1, grid) == '1'
assert calcudoku.display_grid(2, grid) == '1 2\n4 5'
assert calcudoku.display_grid(3, grid) == '1 2 3\n4 5 6\n7 8 9'

assert calcudoku.zero_checker([1, 5, 8], grid, 3) == True
assert calcudoku.zero_checker([0, 4, 7], grid, 3) == True
assert calcudoku.zero_checker([1], [[0, 0], [0, 0]], 2) == False

assert calcudoku.make_grid(0) == []
assert calcudoku.make_grid(1) == [[0]]
assert calcudoku.make_grid(2) == [[0, 0], [0, 0]]

assert calcudoku.make_cages('1') == [1]
assert calcudoku.make_cages('1 2') == [1, 2]
assert calcudoku.make_cages('1 2 3') == [1, 2, 3]
