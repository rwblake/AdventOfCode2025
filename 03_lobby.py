#!/usr/bin/env python3


import sys

def maximum_joltage(bank):
	# left-to-right find the biggest first digit (excl final digit). first occurence
	first_digit = '0'
	first_digit_idx = 0
	for i, digit in enumerate(bank[:-1]):
		if digit > first_digit:
			first_digit = digit
			first_digit_idx = i
	# find the largest second digit in the remaining section
	second_digit = max(bank[first_digit_idx+1:])

	maximum_joltage = int(first_digit + second_digit)
	return maximum_joltage


def part_one(banks):
	return sum([maximum_joltage(bank) for bank in banks])


def part_two(banks):
	pass


def main():
	standard_path = "input/03_lobby.txt"
	test_path = "input/03_lobby_test.txt"
	
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

