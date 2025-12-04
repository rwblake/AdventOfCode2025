#!/usr/bin/env python3


import sys


DIRECTIONS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
PAPER = '@'


def get(x, y, grid):
	return grid[y][x]


def neighbours(x, y, width, height):
	neighbours = [[x+dx, y+dy] for dx, dy in DIRECTIONS if 0 <= x+dx < width and 0 <= y+dy < height]
	return neighbours


def part_one(grid):
	width = len(grid[0])
	height = len(grid)

	accessible = 0
	for x in range(width):
		for y in range(height):
			if get(x, y, grid) != PAPER:
				continue

			ns = neighbours(x, y, width, height)
			count = sum([get(nx, ny, grid) == PAPER for nx, ny in ns])
			if count < 4:
				accessible += 1
	return accessible


def part_two(lines):
	pass


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

