# Name:		Andres Rodriguez 
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Moonlander
# Term:         Winter 2020
import moonlander

assert moonlander.update_acceleration(1, 5) == 0
assert moonlander.update_acceleration(1, 10) == 1.62
assert moonlander.update_acceleration(1, 15) == 3.24

assert moonlander.update_altitude(0, 0, 0) == 0
assert moonlander.update_altitude(4, 5, 6) == 12
assert moonlander.update_altitude(1, 1, 0) == 2

assert moonlander.update_velocity(0, 0) == 0
assert moonlander.update_velocity(0, 1) == 1
assert moonlander.update_velocity(1, 2) == 3

assert moonlander.update_fuel(1, 2) == 0
assert moonlander.update_fuel(2, 2) == 0
assert moonlander.update_fuel(3, 2) == 1
