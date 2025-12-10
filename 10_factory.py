#!/usr/bin/env python3


import sys
from collections import defaultdict


def parse(lines):
	machines = []
	for line in lines:
		tmp = line.split()
		light_diagram = tmp[0]
		button_wiring = tmp[1:-1]
		joltages = tmp[-1]

		light_diagram = light_diagram.strip("[]")
		button_wiring = map(lambda x: x.strip("()"), button_wiring)
		joltages = joltages.strip("{}")

		light_diagram = tuple([light == '#' for light in light_diagram])
		button_wiring = [tuple(map(int, wiring.split(","))) for wiring in button_wiring]
		joltages = list(map(int, joltages.split(",")))

		machines.append([light_diagram, button_wiring, joltages])
	return machines


def super_neighbours(button_wirings):
	return lambda node: [tuple([not light if i in wiring else light for i, light in enumerate(node)]) for wiring in button_wirings]


def reconstruct_path(came_from, current):
	total_path = []
	while current in came_from:
		current = came_from[current]
		total_path.insert(0, current)
	return total_path


def a_star(start, goal, neighbours):
	# turns out i couldnt think of an admissible heuristic function
	d = 1
	open_set = [start]

	came_from = dict()
	g_score = defaultdict(lambda: float("inf"))
	g_score[start] = 0

	f_score = defaultdict(lambda: float("inf"))
	f_score[start] = h(start)

	while open_set:
		current = min(open_set, key=f_score.get)
		if current == goal:
			return reconstruct_path(came_from, current)

		open_set.remove(current)
		for neighbour in neighbours(current):
			tentative_g_score = g_score[current] + d
			if tentative_g_score < g_score[neighbour]:
				came_from[neighbour] = current
				g_score[neighbour] = tentative_g_score
				f_score[neighbour] = tentative_g_score + 0
				if neighbour not in open_set:
					open_set.append(neighbour)
	raise Exception("no path to goal state")

def part_one(lines):
	machines = parse(lines)
	presses = 0

	# pathfinding via a*
	for light_diagram, button_wiring, joltages in machines:
		path = a_star(light_diagram, tuple([False for _ in light_diagram]), super_neighbours(button_wiring))
		presses += len(path)
	return presses

def part_two(lines):
	pass


def main():
	standard_path = "input/10_factory.txt"
	test_path = "input/10_factory_test.txt"
	
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

