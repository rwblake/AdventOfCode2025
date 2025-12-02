#!/usr/bin/env python3


import sys


def part_one(rotations):
	dial = 50
	zero_count = 0
	for rotation in rotations:
		direction = rotation[0]
		clicks = int(rotation[1:])
		if direction == "L":
			clicks *= -1

		dial = (dial + clicks) % 100
		if dial == 0:
			zero_count += 1
	return zero_count




def part_two(lines):
	pass


def main():
	standard_path = "input/01_secret_entrance.txt"
	test_path = "input/01_secret_entrance_test.txt"
	
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

