"""🎄 Solution for Day 9 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 09.py
"""

import numpy as np
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
    # Ultra-fast parsing using numpy's fromstring on preprocessed data
    data = inp.replace(",", "\n")
    coords = np.fromstring(data, dtype=np.int64, sep="\n").reshape(-1, 2)
    n = len(coords)

    # Generate pairs using triu_indices
    idx = np.triu_indices(n, k=1)
    dx = np.abs(coords[idx[0], 0] - coords[idx[1], 0])
    dy = np.abs(coords[idx[0], 1] - coords[idx[1], 1])

    return int(np.max((dx + 1) * (dy + 1)))


def part2(inp: str) -> str | int | None:
    tiles = []
    for line in inp.splitlines():
        tiles.append(tuple(int(x) for x in line.split(",")))

    raw_polygon = Polygon(tiles)
    shapely.prepare(raw_polygon)

    n = len(tiles)
    tiles_arr = np.array(tiles)

    # Generate all pairs using numpy broadcasting
    idx = np.triu_indices(n, k=1)
    t1 = tiles_arr[idx[0]]
    t2 = tiles_arr[idx[1]]

    # Compute bounds
    min_x = np.minimum(t1[:, 0], t2[:, 0])
    max_x = np.maximum(t1[:, 0], t2[:, 0])
    min_y = np.minimum(t1[:, 1], t2[:, 1])
    max_y = np.maximum(t1[:, 1], t2[:, 1])

    # Compute areas
    areas = (max_x - min_x + 1) * (max_y - min_y + 1)

    # Get indices sorted by area descending
    order = np.argsort(-areas)

    # Check in batches, starting from largest areas
    batch_size = 500
    for start in range(0, len(order), batch_size):
        batch_idx = order[start : start + batch_size]
        boxes = shapely.box(
            min_x[batch_idx], min_y[batch_idx], max_x[batch_idx], max_y[batch_idx]
        )
        contained = shapely.contains(raw_polygon, boxes)

        if np.any(contained):
            valid_in_batch = np.where(contained)[0]
            return int(areas[batch_idx[valid_in_batch[0]]])

    return 0
