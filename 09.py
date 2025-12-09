"""🎄 Solution for Day 9 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 09.py
"""

from shapely.geometry.polygon import Polygon

inp = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
part1_asserts = [
    (inp, 50),
]
part2_asserts = [
    (inp, 24),
]


def part1(inp: str) -> str | int | None:
    tiles = []
    for line in inp.splitlines():
        tiles.append(tuple(int(x) for x in line.split(",")))
    # Using two tiles as opposite corners, what is the largest area of any rectangle you can make?
    largest_area = 0
    n = len(tiles)
    for i in range(n):
        for j in range(n):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            largest_area = max(largest_area, (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1))
    return largest_area


def part2(inp: str) -> str | int | None:
    tiles = []
    for line in inp.splitlines():
        tiles.append(tuple(int(x) for x in line.split(",")))
    polygon = Polygon(tiles)
    largest_area = 0
    n = len(tiles)
    for i in range(n):
        for j in range(n):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            if polygon.contains(Polygon([tiles[i], (x2, y1), tiles[j], (x1, y2)])):
                largest_area = max(
                    largest_area, (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                )
    return largest_area
