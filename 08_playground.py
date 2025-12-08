#!/usr/bin/env python3


import sys
import numpy as np
from itertools import combinations
from operator import mul
from functools import reduce


def parse(lines):
	return [np.array(list(map(int, line.split(',')))) for line in lines]


def merge_box_circuits(a, b, circuits):
	"""merge circuits containing boxes of index a and index b"""
	# find the circuit containting b and remove it from list
	circuit_b = None
	for circuit in circuits:
		if b in circuit and a not in circuit:
			circuit_b = circuit
			circuits.remove(circuit)
			break
	else:
		# if it already contains a then do nothing
		continue
	# merge the circuit with the circuit containing a
	for circuit in circuits:
		if a in circuit:
			circuit.extend(circuit_b)


def part_one(lines):
	boxes     = parse(lines)  # coordinates of boxes
	circuits  = [[i] for i in range(len(boxes))]  # groups of box indices linked together
	pairs     = list(combinations(range(len(boxes)), 2))  # combinations of box indices
	
	# sort pairs by euclidian square distance, shortest first
	distance  = lambda pair: np.sum((boxes[pair[0]]-boxes[pair[1]])**2)
	pairs.sort(key=distance)

	for a, b in pairs[:1000]:
		merge_box_circuits(a, b, circuits)
		
	lengths = map(len, circuits)
	lengths.sort(reverse=True)
	return reduce(mul, lengths[:3])


def part_two(lines):
	boxes     = parse(lines)  # coordinates of boxes
	circuits  = [[i] for i in range(len(boxes))]  # groups of box indices linked together
	pairs     = list(combinations(range(len(boxes)), 2))  # combinations of box indices
	
	# sort pairs by euclidian square distance, shortest first
	distance  = lambda pair: np.sum((boxes[pair[0]]-boxes[pair[1]])**2)
	pairs.sort(key=distance)

	while len(circuits) > 1:
		a, b = pairs.pop(0)
		merge_box_circuits(a, b, circuits)
		
	return boxes[a][0] * boxes[b][0]


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

