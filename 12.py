"""🎄 Solution for Day 12 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 12.py
"""

import math

inp = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""
# part1_asserts = [
#     (inp, 2),
# ]
part2_asserts = [
    (inp, None),
]


def part1(inp: str) -> str | int | None:
    *tiles, regions = inp.strip().split("\n\n")
    tile_counts = {int(tile[0]): tile.count("#") for tile in tiles}
    cnt = 0
    for region in regions.splitlines():
        size, tile_requirements = region.split(": ")
        region_size = math.prod(tuple(int(x) for x in size.split("x")))
        region_space = sum(
            (tile_counts[id_] * int(num))
            for id_, num in enumerate(tile_requirements.split())
        )
        if region_space < region_size:
            cnt += 1
    return cnt


def part2(inp: str) -> str | int | None:
    return None
