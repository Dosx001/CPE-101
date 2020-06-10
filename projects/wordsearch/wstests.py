# Name:		Andres Rodriguez 
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Wordsearch
# Term:         Winter 2020
import wordsearch

assert wordsearch.reverse_string('hello') == 'olleh'
assert wordsearch.reverse_string('computer') == 'retupmoc'
assert wordsearch.reverse_string('nice') == 'ecin'

assert wordsearch.parse_word('computer help not', 0) == 'computer'
assert wordsearch.parse_word('computer help not', 1) == 'help'
assert wordsearch.parse_word('computer help not', 2) == 'not'

assert wordsearch.ms('computer', 0, 10, 3) == 'cpe'
assert wordsearch.ms('NnIiCcEe', 0, 8, 2) == 'NICE'
assert wordsearch.ms('Pizza', 0, 5, 1) == 'Pizza'
#assert wordsearch.ms('Pizza', 0, 5, 0) == 'Pizza'

assert wordsearch.transpose_string('ABCDEFGHI', 3) == 'ADGBEHCFI'
assert wordsearch.transpose_string('123456789', 3) == '147258369'
assert wordsearch.transpose_string('ABCDEFGHIJKLMNOP', 4) == 'AEIMBFJNCGKODHLP'

assert wordsearch.RMS('computer', 0, 10, 3) == 'epc'
assert wordsearch.RMS('NnIiCcEe', 0, 8, 2) == 'ECIN'
assert wordsearch.RMS('Pizza', 0, 5, 1) == 'azziP'

assert wordsearch.FF('asdf', 'sd', 2) == '\nsd: [FF] (0, 1)'
assert wordsearch.FF('abcdefghi', 'ef', 3) == '\n ef: [FF] (1, 1)'
assert wordsearch.FF('asdfefghijklnmop', 'qwe', 4) == ''

assert wordsearch.FD('BNGTEKBYKUOLEZGGELRBERARYLNGUQJEECLUPACEPETOKIWRRHNUWINJEBMOJFRKHWODFIWBKPEWOJEUPODXLACRBRXCKGOECGBB', 'PURPLE', 10) == '\n    PURPLE: [FD] (4, 0)'
assert wordsearch.FD('BNGTEKBYKUOLEZGGELRBERARYLNGUQJEECLUPACEPETOKIWRRHNUWINJEBMOJFRKHWODFIWBKPEWOJEUPODXLACRBRXCKGOECGBB', 'BLUE', 10) == '\n      BLUE: [FD] (0, 6)'
assert wordsearch.FD('SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL', 'fasd', 7) == ''

assert wordsearch.FU('xzdyindaw', 'an', 3, 2) == '\n an: [FU] (2, 1)'
assert wordsearch.FU('xzdyindaw', 'did', 3, 2) == '\ndid: [FU] (2, 0)'
assert wordsearch.FU('xndaizdyw', 'ASD', 3, 2) == ''

assert wordsearch.UU('SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL', 'LIST', 7) == '\n   LIST: [UU] (6, 6)'
assert wordsearch.UU('SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL', 'LIST', 7) == '\n   LIST: [UU] (6, 6)'
assert wordsearch.UU('SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL', 'adsf', 7) == ''

assert wordsearch.BD('xzdyiadnw', 'did', 3, 2) == '\ndid: [BD] (0, 2)'
assert wordsearch.BD('xzdyiadnw', 'an', 3, 2) == '\n an: [BD] (1, 2)'
assert wordsearch.BD('xzdyiadnw', 'ASD', 3, 2) == ''

assert wordsearch.BU('xzdyiadnw', 'wi', 3) == '\n wi: [BU] (2, 2)'
assert wordsearch.BU('xzdyiadnw', 'ny', 3) == '\n ny: [BU] (2, 1)'
assert wordsearch.BU('xzdyiadnw', 'ASD', 3) == ''

assert wordsearch.DD('SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL', 'STR', 7) == '\n    STR: [DD] (0, 0)'
assert wordsearch.DD('SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL', 'STR', 7) == '\n    STR: [DD] (0, 0)'
assert wordsearch.DD('SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL', 'asfds', 7) == ''

assert wordsearch.BB('SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL', 'TUPLE', 7) == '\n  TUPLE: [BB] (3, 6)'
assert wordsearch.BB('SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL', 'TUPLE', 7) == '\n  TUPLE: [BB] (3, 6)'
assert wordsearch.BB('SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL', 'fasd', 7) == ''
