#!/usr/bin/env python3


import sys
import numpy as np
from itertools import combinations


def parse(lines):
	return [np.array(list(map(int, line.split(',')))) for line in lines]


def part_one(lines):
	tiles = parse(lines)
	pairs     = list(combinations(range(len(tiles)), 2))  # combinations of box indices

	area = lambda pair: np.prod(tiles[pair[0]]-tiles[pair[1]]+np.array([1, 1]))
	best_pair = max(pairs, key=area)
	return area(best_pair)


def part_two(lines):
	pass


def main():
	standard_path = "input/09_movie_theater.txt"
	test_path = "input/09_movie_theater_test.txt"
	
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

