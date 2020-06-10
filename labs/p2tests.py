# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set II
# Term:         Winter 2020


import pset2

#pset2.print_hello('work')
#print(len('Hello work'))
#assert len(pset2.print_hello('work')) == len('Hello work')

assert pset2.cube(-1) == -1
assert pset2.cube(0) == 0
assert pset2.cube(1) == 1

assert pset2.do_math(1, 1) == 3.5
assert pset2.do_math(2, 0) == 3
assert pset2.do_math(2, 2) == 5

assert pset2.get_hypotenuse(0, 0) == 0
assert pset2.get_hypotenuse(0, 1) == 1
assert pset2.get_hypotenuse(0, 2) == 2

assert pset2.get_distance(0, 0, 0, 0) == 0
assert pset2.get_distance(0, 0, 0, 1) == 1
assert pset2.get_distance(0, 0, 0, 2) == 2

assert pset2.get_perimeter(0, 0, 0, 0, 0, 0) == 0
assert pset2.get_perimeter(0, 0, 0, 10, 10, 0) == 34.14213562373095
assert pset2.get_perimeter(0, 0, 0, 15, 20, 0) == 60

assert pset2.round_to_hundredths(5555.5555) == 5555.56
assert pset2.round_to_hundredths(.014) == .01
assert pset2.round_to_hundredths(1.1239999) == 1.12

