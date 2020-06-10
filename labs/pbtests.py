# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set XI
# Term:         Winter 2020
import psetb

assert psetb.parse_term("asdSpring 1234fa") == "Spring 1234"
assert psetb.parse_term("asdFall '12a34fa") == "Fall '12"
assert psetb.parse_term("asdWinter 1234fa") == "Winter 1234"

assert psetb.parse_time("afasd12:01:59PMafsd") == "12:01:59PM"
assert psetb.parse_time("afasd02:01AMafsd") == "02:01AM"
assert psetb.parse_time("afasd02:01:59Pafsd") == "02:01:59"

assert psetb.parse_name("fasdSamuel L. Jackson4fdsfa") == "Samuel L. Jackson"
assert psetb.parse_name("asdfaB. D. Wong5afsdf") == "B. D. Wong"
assert psetb.parse_name("fasdfasfAlexandria Ocasio-Cortez3fasd") == "Alexandria Ocasio-Cortez"

assert psetb.parse_math("{0+ c_d}") == "0+ c_d"
assert psetb.parse_math("{a1 - 44}") == "a1 - 44"
assert psetb.parse_math("{b0 *45.67}") == "b0 *45.67"
