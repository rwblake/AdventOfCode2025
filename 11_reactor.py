#!/usr/bin/env python3


import sys
import functools


def num_paths(rack, start, end):
	if start == end:
		return 1

	return sum(num_paths(rack, output, end) for output in rack[start])


def part_one(lines):
	rack = {items[0][:-1]: items[1:] for items in map(lambda x: x.split(), lines)}
	return num_paths(rack, "you", "out")

def part_two(lines):
	rack = {items[0][:-1]: items[1:] for items in map(lambda x: x.split(), lines)}
	
	@functools.cache
	def num_paths(start, end, dac=False, fft=False):
		if start == end:
			return 1 if dac and fft else 0

		if start == "dac":
			dac = True
		if start == "fft":
			fft = True
		return sum(num_paths(output, end, dac, fft) for output in rack[start])
	
	return num_paths("svr", "out")


def main():
	standard_path = "input/11_reactor.txt"
	test_path = "input/11_reactor_test.txt"
	
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

