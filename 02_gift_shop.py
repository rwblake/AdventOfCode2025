#!/usr/bin/env python3


import sys


def part_one(lines):
	id_ranges = lines[0].split(',')
	total = 0
	for id_range in id_ranges:
		first_id, last_id = id_range.split('-')
		first_id, last_id = int(first_id), int(last_id)

		for pid in range(first_id, last_id + 1):
			pid = str(pid)

			# invalid ids repeat a sequence twice exactly
			first_half = pid[:len(pid)//2]
			second_half = pid[len(pid)//2:]
			if first_half == second_half:
				total += int(pid)
	return total


def part_two(lines):
	pass


def main():
	standard_path = "input/02_gift_shop.txt"
	test_path = "input/02_gift_shop_test.txt"
	
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

