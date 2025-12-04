"""🎄 Solution for Day 4 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 04.py
"""

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


def num_adjecents(grid: set[tuple[int, int]], paper: tuple[int, int]) -> int:
    count = 0
    x, y = paper
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if (x + dx, y + dy) in grid:
                count += 1
    return count


def part1(inp: str) -> str | int | None:
    count = 0
    grid = set()
    for i, line in enumerate(inp.splitlines()):
        for j, char in enumerate(line):
            if char == "@":
                grid.add((i, j))
    for paper in grid:
        if num_adjecents(grid, paper) < 4:
            count += 1

    return count


def part2(inp: str) -> str | int | None:
    count = 0
    grid = set()
    for i, line in enumerate(inp.splitlines()):
        for j, char in enumerate(line):
            if char == "@":
                grid.add((i, j))
    while True:
        new_grid = set()
        for paper in grid:
            if num_adjecents(grid, paper) < 4:
                count += 1
            else:
                new_grid.add(paper)
        if new_grid == grid:
            return count
        grid = new_grid
