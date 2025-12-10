#!/usr/bin/env python3


import sys
import numpy as np
from itertools import combinations, pairwise

import matplotlib.pyplot as plt
from tqdm import tqdm


def parse(lines):
	return [np.array(list(map(int, line.split(',')))) for line in lines]


def part_one(lines):
	tiles = parse(lines)
	pairs     = list(combinations(range(len(tiles)), 2))  # combinations of box indices

	area = lambda pair: np.prod(tiles[pair[0]]-tiles[pair[1]]+np.array([1, 1]))
	best_pair = max(pairs, key=area)
	return area(best_pair)


def construct_perimeter(points, margin, clockwise):
	perimeter = []
	points = points.copy()
	points.append(points[0])
	points.append(points[1])
	for l1, l2 in pairwise(pairwise(points)):
		point = l1[1]  # starting point for perimeter is end of the line
		# calculate if left or right turn
		v1 = l1[1] - l1[0]
		v2 = l2[1] - l2[0]
		# sine of cross product indicates left or right
		a = np.append(v1, 0)  # np cross product wants 3d vectors
		b = np.append(v2, 0)
		x = np.cross(a, b)[2]  # and returns vector not scalar
		right_hand_turn = x > 0

		# left turns require a longer perimeter (outside corner)
		# right turns require a shorter perimeter (inside corner)
		v1_unit = v1 / np.linalg.norm(v1)

		if clockwise:
			right_hand_turn = not right_hand_turn

		if right_hand_turn:
			point = point - margin * v1_unit
		else:
			point = point + margin * v1_unit
		# perimeter should be to the left of the line for clockwise
		# or to the right of the line for anticlockwise
		if clockwise:
			theta = np.radians(-90)
		else:
			theta = np.radians(+90)
		s, c = np.sin(theta), np.cos(theta)
		R = np.array([[c, -s], [s, c]])
		point = point + np.dot(R, v1_unit) * margin
		perimeter.append(point)
	return perimeter


def plot_polygon(polygon):
	xs = [point[0] for point in polygon]
	ys = [point[1] for point in polygon]
	# connect last and first vertices
	# by repeating first vertex at end
	xs.append(polygon[0][0])
	ys.append(polygon[0][1])
	plt.plot(xs, ys)

count = 0

def lines_intersect(a, b):
	global count
	count += 1

	p1, p2 = a
	p3, p4 = b

	x1, y1 = p1
	x2, y2 = p2
	x3, y3 = p3
	x4, y4 = p4
	
	# line a = p1 + t * (p2 - p1)
	# line b = p3 + u * (p4 - p3)
	# t and u describe how far along the line segment the intersection point is
	# https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
	t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
	u = - ((x1-x2)*(y1-y3) - (y1-y2)*(x1-x3)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
	return 0 <= u <= 1 and 0 <= t <= 1

def polygons_intersect(a, b):
	a = a.copy()
	b = b.copy()
	a.append(a[0])
	b.append(b[0])

	lines_a = list(pairwise(a))
	lines_b = list(pairwise(b))

	#assert len(lines_a) == 4
	#assert len(lines_b) == 8

	#lines_b = [(np.array([11.5,  0.5]), np.array([11.5,  7.5])), (np.array([11.5,  7.5]), np.array([8.5, 7.5])), (np.array([8.5, 7.5]), np.array([8.5, 5.5])), (np.array([8.5, 5.5]), np.array([1.5, 5.5])), (np.array([1.5, 5.5]), np.array([1.5, 2.5])), (np.array([1.5, 2.5]), np.array([6.5, 2.5])), (np.array([6.5, 2.5]), np.array([6.5, 0.5])), (np.array([6.5, 0.5]), np.array([11.5,  0.5]))]
	return any(lines_intersect(line_a, line_b) for line_a in lines_a for line_b in lines_b)


def filter_pair(pair, tiles, perimeter):
	p1, p3 = tiles[pair[0]], tiles[pair[1]]
	p2 = np.array([p1[0], p3[1]])
	p4 = np.array([p3[0], p1[1]])
	rectangle = [p1, p2, p3, p4]
	return not polygons_intersect(rectangle, perimeter)


def part_two(lines):
	# get locations of red tiles
	tiles = parse(lines)

	# find whether loop is clockwise or anticlockwise
	# clockwise     will have more right turns
	# anticlockwise will have more left turns
	turns = 0
	for edge_a, edge_b in pairwise(pairwise(tiles)):  # iterate over pairs of edges
		a1, a2 = edge_a
		b1, b2 = edge_b
		a = a2 - a1
		b = b2 - b1
		# sine of cross product indicates left or right
		a = np.append(a, 0)  # np cross product wants 3d vectors
		b = np.append(b, 0)
		x = np.cross(a, b)[2]  # and returns vector not scalar
		if x < 0:
			turns += 1
		else:
			turns -= 1
	clockwise = turns < 0  # clockwise has more (positive) right hand turns
	# create a perimeter polygon just outside of the edge of the tiles
	margin = 0.5
	perimeter = construct_perimeter(tiles, margin, clockwise)

	# remove sections of overlapping lines
	# TBC

	# make list of possible rectangles
	pairs     = list(combinations(range(len(tiles)), 2))  # combinations of box indices
	
	# find best areas
	area = lambda pair: np.prod(np.abs(tiles[pair[0]]-tiles[pair[1]])+np.array([1, 1]))
	pairs.sort(key=area, reverse=True)

	# filter areas which don't intersect the perimeter polygon
	for pair in tqdm(pairs):
		if filter_pair(pair, tiles, perimeter):
			best_pair = pair
			break
	
	p1, p3 = tiles[best_pair[0]], tiles[best_pair[1]]
	p2 = np.array([p1[0], p3[1]])
	p4 = np.array([p3[0], p1[1]])
	rectangle = [p1, p2, p3, p4]
	print(rectangle)
	plot_polygon(rectangle)
	
	plot_polygon(perimeter)
	plot_polygon(tiles)
	plt.show()
	return area(best_pair)


def main():
	standard_path = "input/09_movie_theater.txt"
	test_path = "input/09_movie_theater_test.txt"
	
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

