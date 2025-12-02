#!/usr/bin/env python3


import sys


def part_one(lines):
	pass


def part_two(lines):
	pass


def main():
	standard_path = "[INPUT_PATH_PLACEHOLDER]"
	test_path = "[TEST_PATH_PLACEHOLDER]"
	
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

