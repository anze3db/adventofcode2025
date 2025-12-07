"""🎄 Solution for Day 4 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 04.py
"""

from collections import deque

import numpy as np
from scipy.ndimage import convolve

inp = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
part1_asserts = [
    (inp, 13),
]
part2_asserts = [
    (inp, 43),
]

NEIGHBORS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
KERNEL = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.int8)


def part1(inp: str) -> str | int | None:
    grid = np.array(
        [[c == "@" for c in line] for line in inp.splitlines()], dtype=np.int8
    )
    neighbor_counts = convolve(grid, KERNEL, mode="constant", cval=0)
    return int(np.sum((grid == 1) & (neighbor_counts < 4)))


def part2(inp: str) -> str | int | None:
    lines = inp.splitlines()
    height, width = len(lines), len(lines[0])

    # Pad the grid with zeros to avoid bounds checking
    pw = width + 2  # padded width
    grid_np = np.pad(
        np.array([[c == "@" for c in line] for line in lines], dtype=np.int8),
        1,
        mode="constant",
        constant_values=0,
    )
    nc_np = convolve(grid_np, KERNEL, mode="constant", cval=0)

    # Flatten for faster 1D indexing
    grid = grid_np.ravel().tolist()
    nc = nc_np.ravel().tolist()

    # Neighbor offsets for padded grid
    offsets = (-pw - 1, -pw, -pw + 1, -1, 1, pw - 1, pw, pw + 1)

    # Find initial movable cells (skip padding)
    to_check = deque()
    for x in range(1, height + 1):
        base = x * pw
        for y in range(1, width + 1):
            idx = base + y
            if grid[idx] and nc[idx] < 4:
                to_check.append(idx)

    count = 0
    pop = to_check.popleft
    push = to_check.appendleft

    while to_check:
        idx = pop()
        if not grid[idx] or nc[idx] >= 4:
            continue

        count += 1
        grid[idx] = 0

        # Update all 8 neighbors - no bounds check needed due to padding
        for offset in offsets:
            n = idx + offset
            if grid[n]:
                nc[n] -= 1
                if nc[n] < 4:
                    push(n)

    return count
