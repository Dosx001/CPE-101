# Name:         Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Pixel Magic
# Term:         Winter 2020
import pixelmagic 

x = [[0, 0, 0]]
y = [[0, 0, 0], [1, 1, 1]]
z = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]]

assert pixelmagic.gray([[1, 1, 1]]) == [[1, 1, 1]]
assert pixelmagic.gray([[2, 2, 2]]) == [[2, 2, 2]]
assert pixelmagic.gray([[3, 3, 3]]) == [[3, 3, 3]]

assert pixelmagic.fade(x, '1', '1', '1', 1) == [[0, 0, 0]]
assert pixelmagic.fade(y, '1', '1', '1', 1) == [[0, 0, 0],
						 [0, 0, 0]]
assert pixelmagic.fade(z, '1', '1', '1', 2) == [[0, 0, 0],
			 [0, 0, 0], [0, 0, 0], [3, 3, 3]]

assert pixelmagic.flip(list(x), 0, 0) == [[0, 0, 0]]
assert pixelmagic.flip(list(y), 2, 1) == [[1, 1, 1], [0, 0, 0]]
assert pixelmagic.flip(list(z), 2, 2) == [[1, 1, 1], [0, 0, 0],
					 [3, 3, 3], [2, 2, 2]]

assert pixelmagic.trans_rev(x, 1) == [[0, 0, 0]]
assert pixelmagic.trans_rev(y, 1) == [[1, 1, 1],
					 [0, 0, 0]]
assert pixelmagic.trans_rev(z, 2) == [[2, 2, 2], 
			[0, 0, 0], [3, 3, 3], [1, 1, 1]]

assert pixelmagic.turn(x, 1, 1, 90) == [[0, 0, 0]]
assert pixelmagic.turn(y, 1, 2, 90) == [[1, 1, 1], [0, 0, 0]]
assert pixelmagic.turn(z, 2, 2, 360) == [[0, 0, 0],
			 [1, 1, 1], [2, 2, 2], [3, 3, 3]]

assert pixelmagic.blur(x, 1, 1) == [[0, 0, 0]]
assert pixelmagic.blur(y, 1, 2) == [[0, 0, 0], [0, 0, 0]]
assert pixelmagic.blur(z, 1, 2) == [[1, 1, 1], [1, 1, 1],
					 [1, 1, 1], [1, 1, 1]]
