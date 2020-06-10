# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set V
# Term:         Winter 2020
import pset5

assert pset5.reverse_string('hello') == 'olleh'
assert pset5.reverse_string('computer') == 'retupmoc'
assert pset5.reverse_string('nice') == 'ecin'

assert pset5.translate_string('hello', 'l', 'p') == 'heppo'
assert pset5.translate_string('computer', 'e', 'o') == 'computor'
assert pset5.translate_string('nice', 'c', 'z') == 'nize'

assert pset5.rotate_chars('a', 13) == 'n'
assert pset5.rotate_chars('A', 13) == 'N'
assert pset5.rotate_chars('abcABCxyzXYZ!@#', 2) == 'cdeCDEzabZAB!@#'
assert pset5.rotate_chars('YyZz', 27) == 'ZzAa'
assert pset5.rotate_chars('qrstQRST', 14) == 'efghEFGH'

assert pset5.encode_ascii('abc') == '097098099'
assert pset5.encode_ascii('ABC') == '065066067'
assert pset5.encode_ascii('nice') == '110105099101'

assert pset5.parse_word('computer help not', 0) == 'computer'
assert pset5.parse_word('computer help not', 1) == 'help'
assert pset5.parse_word('computer help not', 2) == 'not'

assert pset5.swap_chars('inec!') == 'nice!'
assert pset5.swap_chars('2143') == '1234'
assert pset5.swap_chars('hello') == 'ehllo'

assert pset5.is_palindrome('racecar') == True
assert pset5.is_palindrome('tacocat') == True
assert pset5.is_palindrome('nice') == False

assert pset5.decode_ascii('098') == 'b'
assert pset5.decode_ascii('108') == 'l'
assert pset5.decode_ascii('065066067') == 'ABC'
assert pset5.decode_ascii('097098099100') == 'abcd'

assert pset5.make_substring('computer', 0, 10, 3) == 'cpe'
assert pset5.make_substring('NnIiCcEe', 0, 8, 2) == 'NICE'
assert pset5.make_substring('Pizza', 0, 5, 1) == 'Pizza'

assert pset5.longest_substring('hello', 'heel') == 'he'
assert pset5.longest_substring('car', 'are') == 'ar'
assert pset5.longest_substring('make', 'cake') == 'ake'
assert pset5.longest_substring('broke', 'broken') == 'broke'

assert pset5.transpose_string('ABCDEFGHI', 3) == 'ADGBEHCFI'
assert pset5.transpose_string('123456789', 3) == '147258369'
assert pset5.transpose_string('ABCDEFGHIJKLMNOP', 4) == 'AEIMBFJNCGKODHLP'
