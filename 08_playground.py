#!/usr/bin/env python3


import sys
from itertools import combinations
import numpy as np
from operator import mul
from functools import reduce


def parse(lines):
	return [np.array(list(map(int, line.split(',')))) for line in lines]


def part_one(lines):
	boxes     = parse(lines)
	circuits  = [[i] for i in range(len(boxes))]
	pairs     = list(combinations(range(len(boxes)), 2))
	distance  = lambda pair: np.sum((boxes[pair[0]]-boxes[pair[1]])**2)
	pairs.sort(key=distance)
	for a, b in pairs[:1000]:
		circuit_b = None
		for circuit in circuits:
			if b in circuit and a not in circuit:
				circuit_b = circuit
				circuits.remove(circuit)
				break
		else:
			continue
		for circuit in circuits:
			if a in circuit:
				circuit.extend(circuit_b)

	circuits.sort(key=len, reverse=True)
	return reduce(mul, map(len, circuits[:3]))


def part_two(lines):
	pass


def main():
	standard_path = "input/08_playground.txt"
	test_path = "input/08_playground_test.txt"
	
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

