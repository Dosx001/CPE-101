# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set IV	
# Term:         Winter 2020
import pset4

assert pset4.mul(1, 5) == 5
assert pset4.mul(2, 2) == 4
assert pset4.mul(5, 5) == 25

assert pset4.exp(0, 0) == 0
assert pset4.exp(1, 1) == 1
assert pset4.exp(2, 2) == 4 

assert pset4.div(1, 1) == 1
assert pset4.div(2, 2) == 1
assert pset4.div(4, 2) == 2

assert pset4.mod(2, 1) == 0
assert pset4.mod(3, 2) == 1
assert pset4.mod(5, 3) == 2

assert pset4.gcd(1, 1) == 1
assert pset4.gcd(2, 8) == 2
assert pset4.gcd(4, 4) == 4

assert pset4.is_prime(1) == False
assert pset4.is_prime(4) == False
assert pset4.is_prime(17) == True 

assert pset4.sum_ints(2, 11, 3) == 15
assert pset4.sum_ints(1, 10, 1) == 45
assert pset4.sum_ints(1, 20, 6) == 40

assert pset4.sum_mul_table(3) == 36
assert pset4.sum_mul_table(4) == 100
assert pset4.sum_mul_table(5) == 225

assert pset4.rotate_string('computer', 5) == 'putercom'
assert pset4.rotate_string('hello', 5) == 'hello'
assert pset4.rotate_string('nice', 69) == 'enic'

assert pset4.weave_strings('cmue', 'optr') == 'computer'
assert pset4.weave_strings('sine', 'cec') == 'science'
assert pset4.weave_strings('nc', 'ie!') == 'nice!'

assert pset4.to_pig_latin('INTEGER') == 'INTEGERYAY'
assert pset4.to_pig_latin('FLOAT') == 'OATFLAY'
assert pset4.to_pig_latin('NICE') == 'ICENAY'
assert pset4.to_pig_latin('CRY') == 'CRYAY'
