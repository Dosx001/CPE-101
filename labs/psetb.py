# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set XI
# Term:         Winter 2020
import re


def parse_term(text):
	m = re.search(r"(Fall|Winter|Spring|Summer) ('[0-9]{2}|[0-9]{4})", text)
	return m.group()


def parse_time(text):
	m = re.search(r"([1][0-2]|[0][1-9]):[0-5][0-9](:[0-5][0-9])?(AM|PM)?", text)
	return m.group()


def parse_name(text):
	R = r"(VI*|IV|I+)"
	name = r"[A-Z][a-z]+"
	dot = r"[A-Z]\."
	m = re.search(rf"({dot}|{name}) ({dot}|{name})? ?({name}-{name}|{name})( {R})?", text)
	return m.group()


def parse_math(text):
	op = r"(\+|-|\*\*|\*|//|/|%)"
	flt = r"[0-9]*\.[0-9]+"
	alp_num = r"[A-za-z][a-z0-9]*"
	under = rf"{alp_num}_[A-za-z0-9]+"
	stuff = r"[A-Za-z0-9_.]+"
	var = rf"({flt}|{under}|{alp_num}|[0-9]+)"
#	m = re.search(rf"-?{var} *?{op} *?-?{var}", text)
	m = re.search(rf"-?{stuff} *?{op} *?-?{stuff}", text)
	return m.group()
