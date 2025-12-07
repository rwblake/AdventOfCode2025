#!/usr/bin/env python3


import sys
from collections import Counter


BEAM     = 'S'
SPLITTER = '^'


def parse(lines):
	height    = len(lines)

	beams     = []
	splitters = []
	for y, line in enumerate(lines):
		for x, cell in enumerate(line):
			if   cell == BEAM:
				beams.append((x, y))
			elif cell == SPLITTER:
				splitters.append((x, y))

	return beams, splitters, height


def step(beam, splitters):
	"""calculate new beam locations after 1 time step"""
	beam = (beam[0], beam[1] + 1)
	if beam in splitters:
		beam_left  = (beam[0] - 1, beam[1])
		beam_right = (beam[0] + 1, beam[1])
		beams = [beam_left, beam_right]
	else:
		beams = [beam]
	return beams


def part_one(lines):
	beams, splitters, height = parse(lines)
	splits = 0
	for time_step in range(height):
		new_beams = []
		for beam in beams:
			beam_step = step(beam, splitters)
			if len(beam_step) == 2:
				splits += 1
			for new_beam in beam_step:
				if new_beam not in new_beams:
					new_beams.append(new_beam)
		beams = new_beams
	return splits


def part_two(lines):
	# naiive solution has exponential time, space, complexity
	# instead of computing multiple times the same beam, add a count to it
	beams, splitters, height = parse(lines)
	beams = Counter(beams)

	for time_step in range(height):
		new_beams = Counter()

		for beam, count in beams.items():
			beam_step = step(beam, splitters)
			for beam in beam_step:
				new_beams[beam] += count

		beams = new_beams
		
	return sum(beams.values())


def main():
	standard_path = "input/07_laboratories.txt"
	test_path = "input/07_laboratories_test.txt"
	
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

