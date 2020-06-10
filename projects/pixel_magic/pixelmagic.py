# Name:         Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Pixel Magic
# Term:         Winter 2020

import sys
from typing import List


def main(argv: List[str]) -> None:
	fp = Error(argv)
	if fp == None:
		return None
	P = fp.readline()
	size = list(fp.readline().split())
	co_ran = fp.readline()
	pixels = [fp.readline().split() for i in range(int(size[0]) * int(size[1]))]
	for i in range(len(pixels)):
		pixels[i][0] = int(pixels[i][0])
		pixels[i][1] = int(pixels[i][1])
		pixels[i][2] = int(pixels[i][2])
	if argv[1] == 'gray':
		e_pixels = gray(pixels)
	elif argv[1] == 'fade':
		e_pixels = fade(pixels, argv[4], argv[3], argv[5], int(size[0]))
	elif argv[1] == 'flip':
		e_pixels = flip(pixels, int(size[0]), int(size[1]))
	elif argv[1] == 'turn':
		e_pixels = turn(pixels, int(size[0]), int(size[1]), argv[3])
	else:
		try:
			reach = int(argv[3])
			e_pixels = blur(pixels, reach, int(size[0]))
		except IndexError:
			e_pixels = blur(pixels, 4, int(size[0]))
	if argv[1] == 'turn' and (int(argv[3]) // 90) % 2 == 1:
		size[0], size[1] = size[1], size[0]
	image_maker(P, size, co_ran, e_pixels, argv[1])
	fp.close()
	

#def mode(pixels, argv, width, height):
#	if argv[1] == 'gray':
#		return gray(pixels)
#	elif argv[1] == 'fade':
#		return fade(pixels, argv[4], argv[3], argv[5], width)
#	elif argv[1] == 'flip':
#		return flip(pixels, width, height)
#	elif argv[1] == 'turn':
#		return turn(pixels, width, height, argv[3])
#	else:
#		try:
#			return blur(pixels, argv[3], width, height)
#		except IndexError:
#			return blur(pixels, 4, width, height)


def blur(pixels, reach, width):
	e_pixels = []
	for i in range(len(pixels)):
		x = []
		r = g = b = 0
		for ii in range(-reach, reach + 1, 1):
			try:
				pixels[i + ii * width]
				if 0 <= i + ii * width:
					for iii in range(-(i % width) if i % width < reach else -reach,
					width - i % width if width - i % width <= reach else reach + 1, 1):
						x.append(pixels[i + ii * width + iii])
			except IndexError:
				None
		for i in x:
			r += i[0]
			g += i[1]
			b += i[2]
		y = len(x)
		e_pixels.append([int(r / y), int(g / y), int(b / y)])
	return e_pixels


#def turn2(pixels, width, height, deg):
#	start = pixels.index(pixels[-width])
#	e_pixels = []
#	for i in range(int(deg) // 90):
#		e_pixels = [pixels[start - ii * width + i]
#			for i in range(width) for ii in range(height)]
#	return e_pixels


def turn(pixels, width, height, deg):
	for i in range(int(deg) // 90):
		pixels = trans_rev(pixels, width)
		width , height = height, width
	return pixels


def trans_rev(pixels, width):
	e_pixels = []
	x = []
	n = m = o = 0
	for i in pixels:
		x.append(pixels[n + m])
		m += width
		o += 1
		if o == len(pixels) / width:
			n += 1
			m = o = 0
			e_pixels += x[::-1]
			x = []
	return e_pixels


def flip(pixels, width, height):
	m = 0
	for i in range(height):
		n = width - 1
		for ii in range(width // 2 + width % 2):
			pixels[i + ii + m], pixels[i + n + m
			] = pixels[i + n + m], pixels[i + ii + m]
			n -= 1
		m += width - 1
	return pixels


def fade(pixels, x, y, r, width):
	e_pixels = []
	x, y, r = int(x), int(y), int(r)
	for i in range(len(pixels)):
		d = ((x - i % width) ** 2 + (y - i // width) ** 2) ** .5
		m = (r - d) / r
		if .2 <= m:
			e_pixels.append([int(pixels[i][0] * m),
			int(pixels[i][1] * m), int(pixels[i][2] * m)])
		else:
			e_pixels.append([int(pixels[i][0] * .2),
			int(pixels[i][1] * .2), int(pixels[i][2] * .2)])
	return e_pixels


def gray(pixels):
	e_pixels = []
	for i in pixels:
		avg = int((i[0] + i[1] + i[2]) / 3)
		e_pixels.append([avg, avg, avg])
	return e_pixels


def image_maker(P, size, co_ran, pixels, mode): 
	fp2 = open(f'{mode}.ppm', 'w')
	fp2.write(f'{P}')
	fp2.write(f'{size[0]} {size[1]}\n')
	fp2.write(f'{co_ran}')
	for i in pixels:
		fp2.write(f'{i[0]} {i[1]} {i[2]}\n')
	fp2.close()


def Error(argv):
	try:
		if len(argv) < 3:
			return print('Usage: python3 pixelmagic.py <mode> <image>')
		fp = open(argv[2])
		if not argv[1] in ['gray', 'fade', 'flip', 'turn', 'blur']:
			return print('Error: Invalid mode')
		if argv[1] == 'fade' and len(argv) < 6:
			return print('Usage: python3 pixelmagic.py fade <image> <row> <col> <radius>')
		elif argv[1] == 'turn' and len(argv) < 4:
			return print('Usage: python3 pixelmagic.py turn <image> <degree>')
		elif argv[1] == 'turn' and int(argv[3]) % 90 != 0:
			return print('Error: Turn must be in 90 degree increments')
		return fp
	except FileNotFoundError:
		return print(f'Error: Unable to open {argv[2]}')


if __name__ == "__main__":
    main(sys.argv)
