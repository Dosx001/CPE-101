# Name:		Andres Rodriguez 
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Calcudoku
# Term:         Winter 2020


def main():
	n_cages = int(input())
	cages = []
	for i in range(n_cages): #gives number of cages
		x = input()
		cages.insert(i, make_cages(x))
	grid_size = grid_size_finder(n_cages, cages)
	grid = make_grid(grid_size) 
	m = -1
	while m != grid_size ** 2 - 1: #changes grid values
		m += 1 # m-1 gives index for loc #?????
		grid[m // grid_size][m % grid_size] += 1
		col = get_col(grid, grid_size, m)
		row = grid[m // grid_size] #finds row
		for i in range(n_cages): #gives current cage #s and sum 
			if m in cages[i][1:]:
				cage = cages[i][1:]
				sum_cage = cages[i][0]	
		if  grid_size < grid[m // grid_size][m % grid_size]:
			grid[m // grid_size][m % grid_size] = 0
			m -= 2 	
		elif has_duplicates(row) or has_duplicates(col):
			m -= 1
		else:
			check = zero_checker(cage, grid, grid_size)
			if check == True:
				Sum = cage_sum(cage, grid, grid_size)
				if Sum != sum_cage:
					m -= 1
	return print(display_grid(grid_size, grid))


def get_col(grid, grid_size, m):
	col = []
	for i in range(grid_size): #finds col
		col.insert(i, grid[i][m % grid_size])	
	return col


def cage_sum(cage, grid, grid_size):
	Sum = 0
	for i in range(len(cage)):
		x = cage[i]
		Sum += grid[x // grid_size][x % grid_size] 	
	return Sum


def grid_size_finder(n_cages, cages):
	x = 0
	for i in range(n_cages): #gives number for NxN grid
		y = cages[i][1:]
		for ii in y:
			if x < ii:
				x = ii
	return int((x + 1) ** (1 / 2))


def display_grid(grid_size, grid):
	final = ''
	for i in range(grid_size): #display grid
		for ii in range(grid_size):
			if grid_size - 1 == ii:
				final += str(grid[i][ii])
			else:	
				final += str(grid[i][ii]) + ' '
			if ii == grid_size - 1 and i != grid_size - 1:
				final += '\n'
	return final


def zero_checker(cage, grid, grid_size):
	check = True
	for i in range(len(cage)):
		x = cage[i]
		if grid[x // grid_size][x % grid_size] == 0:
			check *= False
	return check


def make_grid(grid_size):
	grid = []
	for i in range(grid_size):
		a = []
		for i in range(grid_size):
			a.insert(i, 0)
		grid.insert(i, a)
	return grid


def make_cages(cage):
	cages = []
	x = cage
	z = []
	for ii in range(x.count(' ') + 1):
		z.insert(ii, int(parse_word(x, ii)))
	return z


def parse_word(word, n):
	m = -1
	new = ''
	for i in word:
		if i != ' ':
			new = new + i
			work = new
		else:
			m += 1
			new = ''
		if m == n:
			break
	return work


def has_duplicates(x):
	for i in x:
		if 0 < i and 1 < x.count(i):
			return True
	return False


if __name__ == '__main__':
	main()
