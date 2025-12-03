#!/usr/bin/env python3


import sys


def maximum_joltage_iterative(bank, n=2):
	maximum_joltage = ""
	for digit_idx in range(1, n):
		best = '0'
		count = 0
		for i, digit in enumerate(bank[:-(n-digit_idx)]):  # for the first digit exclude the last n-1 places etc
			if digit > best:
				best = digit
				count = i + 1
		maximum_joltage += best
		for _ in range(count):
			bank = bank[1:]
	maximum_joltage += max(bank)
	maximum_joltage = int(maximum_joltage)
	return maximum_joltage

def maximum_joltage_recursive(bank, n=2):
	# base case
	if n == 1:
		return max(bank)

	# find the earliest greatest digit
	# excluding the last (n-1) digits
	digit = max(bank[:1-n])
	# prune off up to the digit you found (inclusive)
	i = bank.index(digit)
	# recurse, decrementing n
	return digit + maximum_joltage_recursive(bank[i+1:], n-1)

def maximum_joltage(bank, n=2):
	return int(maximum_joltage_recursive(bank, n))


def part_one(banks):
	return sum([maximum_joltage(bank) for bank in banks])


def part_two(banks):
	return sum([maximum_joltage(bank, n=12) for bank in banks])


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

