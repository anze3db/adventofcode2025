"""🎄 Solution for Day 9 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 09.py
"""

from itertools import combinations

import shapely
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
        for j in range(i + 1, n):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            largest_area = max(largest_area, (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1))
    return largest_area


def part2(inp: str) -> str | int | None:
    tiles = []
    for line in inp.splitlines():
        tiles.append(tuple(int(x) for x in line.split(",")))

    raw_polygon = Polygon(tiles)
    shapely.prepare(raw_polygon)  # Prepare for faster containment checks

    candidates = []

    for (x1, y1), (x2, y2) in combinations(tiles, 2):
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        min_x, max_x = (x1, x2) if x1 < x2 else (x2, x1)
        min_y, max_y = (y1, y2) if y1 < y2 else (y2, y1)
        candidates.append((area, min_x, min_y, max_x, max_y))

    # Sort by area descending
    candidates.sort(reverse=True)

    # Use shapely vectorized contains - check in batches of decreasing area
    batch_size = len(candidates) // 10
    for start in range(0, len(candidates), batch_size):
        batch = candidates[start : start + batch_size]
        rects = shapely.box(
            [c[1] for c in batch],
            [c[2] for c in batch],
            [c[3] for c in batch],
            [c[4] for c in batch],
        )

        contained = shapely.contains(raw_polygon, rects)

        # Find first (largest area) that is contained
        for i, is_contained in enumerate(contained):
            if is_contained:
                return batch[i][0]

    return 0
