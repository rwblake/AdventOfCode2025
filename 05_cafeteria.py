#!/usr/bin/env python3


import sys


def parse(lines):
	fresh_ranges = []
	ingredients = []
	ingredient = False
	for line in lines:
		if line == "":
			ingredient = True
			continue
		if ingredient:
			ingredients.append(int(line))
		else:
			l, h = line.split('-')
			l, h = int(l), int(h)
			fresh_ranges.append(range(l, h+1))
	return ingredients, fresh_ranges


def part_one(lines):
	ingredients, fresh_ranges = parse(lines)
	return sum([any([ingredient in fresh_range for fresh_range in fresh_ranges]) for ingredient in ingredients])


def part_two(lines):
	pass


def main():
	standard_path = "input/05_cafeteria.txt"
	test_path = "input/05_cafeteria_test.txt"
	
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

