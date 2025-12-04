#!/usr/bin/env python3


import sys


DIRECTIONS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
PAPER = '@'


def get(x, y, grid):
	return grid[y][x]


def remove(x, y, grid):
	row = list(grid[y])
	row[x] = '.'
	grid[y] = ''.join(row)


def neighbours(x, y, width, height):
	neighbours = [[x+dx, y+dy] for dx, dy in DIRECTIONS if 0 <= x+dx < width and 0 <= y+dy < height]
	return neighbours


def accessible(x, y, grid):
	width, height = len(grid[0]), len(grid)
	ns = neighbours(x, y, width, height)
	count = sum([get(nx, ny, grid) == PAPER for nx, ny in ns])
	return count < 4


def part_one(grid):
	width = len(grid[0])
	height = len(grid)

	num_accessible = 0
	for x in range(width):
		for y in range(height):
			if get(x, y, grid) != PAPER:
				continue

			if accessible(x, y, grid):
				num_accessible += 1
	return num_accessible


def part_two(grid):
	width = len(grid[0])
	height = len(grid)

	removed_total = 0
	while True:
		removed = 0
		for x in range(width):
			for y in range(height):
				if get(x, y, grid) != PAPER:
					continue

				if accessible(x, y, grid):
					remove(x, y, grid)
					removed += 1
		removed_total += removed

		if removed == 0:
			break
	return removed_total

def main():
	standard_path = "input/04_printing_department.txt"
	test_path = "input/04_printing_department_test.txt"
	
	if "t" in sys.argv:
		path = test_path
	else:
		path = standard_path

	with open(path, "r") as f:
		lines = f.read().splitlines()

	if "1" in sys.argv:
		print(part_one(lines))
	elif "2" in sys.argv:	
		print(part_two(lines))
	else:
		print(part_one(lines))
		print(part_two(lines))


if __name__ == "__main__":
	main()

