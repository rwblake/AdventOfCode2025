#!/usr/bin/env python3


import sys
import numpy as np
from functools import reduce


def part_one(lines):
	# remove whitespace
	lines = map(lambda x: x.split(), lines)
	# rotate (kinda)
	lines = zip(*lines)

	total = 0
	for problem in lines:
		operator = problem[-1]
		values   = map(int, problem[:-1])

		if operator == '*':
			func = lambda x, y: x * y
		elif operator == '+':
			func = lambda x, y: x + y
			
		result   = reduce(func, values)
		total += result
	return total


def part_two(lines):
	pass


def main():
	standard_path = "input/06_trash_compactor.txt"
	test_path = "input/06_trash_compactor_test.txt"
	
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

