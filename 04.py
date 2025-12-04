"""🎄 Solution for Day 4 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 04.py
"""

from collections import deque

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

NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def can_move(grid: set[tuple[int, int]], paper: tuple[int, int]) -> bool:
    count = 0
    x, y = paper
    for dx, dy in NEIGHBORS:
        if (x + dx, y + dy) in grid:
            count += 1
            if count >= 4:
                return False
    return True


def part1(inp: str) -> str | int | None:
    count = 0
    grid = set()
    for i, line in enumerate(inp.splitlines()):
        for j, char in enumerate(line):
            if char == "@":
                grid.add((i, j))
    for paper in grid:
        if can_move(grid, paper):
            count += 1

    return count


def part2(inp: str) -> str | int | None:
    count = 0
    grid = set()
    for i, line in enumerate(inp.splitlines()):
        for j, char in enumerate(line):
            if char == "@":
                grid.add((i, j))

    to_check = deque(grid)

    while to_check:
        paper = to_check.popleft()
        if paper not in grid:
            continue
        neighbors = []
        for dx, dy in NEIGHBORS:
            neighbor = (paper[0] + dx, paper[1] + dy)
            if neighbor in grid:
                neighbors.append(neighbor)

        if len(neighbors) >= 4:
            continue

        count += 1
        grid.remove(paper)
        for neighbor in neighbors:
            to_check.appendleft(neighbor)

    return count
