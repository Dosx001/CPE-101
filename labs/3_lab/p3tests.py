# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set III
# Term:         Winter 2020
import pset3

assert pset3.is_positive(1) == True 
assert pset3.is_positive(5) == True 
assert pset3.is_positive(-1) == False

assert pset3.both_positive(1, 2) == True
assert pset3.both_positive(-1, 1) == False
assert pset3.both_positive(-1, -1) == False 

assert pset3.is_triangle(1, 2, 3) == False
assert pset3.is_triangle(2, 2, 3) == True
assert pset3.is_triangle(2, 3, 4) == True

assert pset3.is_isosceles_triangle(2, 2, 3) == True
assert pset3.is_isosceles_triangle(3, 3, 5) == True
assert pset3.is_isosceles_triangle(4, 4, 8) == False

assert pset3.is_int(1) == True
assert pset3.is_int(1.21) == False
assert pset3.is_int(1.4) == False 

assert pset3.abs_val(-1) == 1
assert pset3.abs_val(1) == 1
assert pset3.abs_val(0) == 0

assert pset3.is_rotation("dwor", "word") == True
#assert pset3.is_rotation("word", "word") == False
assert pset3.is_rotation("wodr", "word") == False
assert pset3.is_rotation("rdwo", "word") == True
#assert pset3.is_rotation("is", "isi") == False

assert pset3.max_of_two(1, 2) == 2 
assert pset3.max_of_two(0, 2) == 2
assert pset3.max_of_two(100, 50) == 100

assert pset3.max_of_three(1, 2, 3) == 3
assert pset3.max_of_three(5, 6, 4) == 6
assert pset3.max_of_three(88, 64, 10) == 88

assert pset3.mix_colors("red", "blue") == "purple"
assert pset3.mix_colors("yellow", "blue") == "green"
assert pset3.mix_colors("red", "yellow") == "orange"
assert pset3.mix_colors("red", "red") == "red"

assert pset3.find_discriminant(1, 1, 1) == None
assert pset3.find_discriminant(1, 10, 1) == 96
assert pset3.find_discriminant(1, 0, 0) == 0


assert pset3.solve_poly(1, 1, 1) == None
assert pset3.solve_poly(1, 0, 0) == 0
assert abs(pset3.solve_poly(1, -15, 5) - 14.6589) < 1e-3
assert abs(pset3.solve_poly(1, -11, 1) - 10.9083) < 1e-3
assert pset3.solve_poly(0, -11, 1) == None
assert pset3.solve_poly(-1, 2, -1) == 1
assert pset3.solve_poly(3, 3, 3) == None
assert pset3.solve_poly(12, 5, 45) == None
