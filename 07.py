"""🎄 Solution for Day 7 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 07.py
"""

inp = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
part1_asserts = [
    (inp, 21),
]
part2_asserts = [
    (inp, 40),
]


def part1(inp: str) -> str | int | None:
    beams: set[tuple[int, int]] = set()
    splitters: set[tuple[int, int]] = set()
    for i, line in enumerate(inp.splitlines()):
        for j, c in enumerate(line):
            if c == "S":
                beams.add((j, i))
            elif c == "^":
                splitters.add((j, i))
    max_splitter_y = max(y for _, y in splitters)
    last_y = max(y for _, y in beams)
    cnt = 0
    while max_splitter_y >= last_y:
        new_beams = set()
        for cx, cy in beams:
            if (cx, cy) in splitters:
                new_beams.add((cx - 1, cy + 1))
                new_beams.add((cx + 1, cy + 1))
                cnt += 1
            else:
                new_beams.add((cx, cy + 1))

        beams = new_beams
        last_y = next(y for _, y in beams)
    return cnt


def part2(inp: str) -> str | int | None:
    beams: dict[tuple[int, int], int] = {}
    splitters: set[tuple[int, int]] = set()
    for i, line in enumerate(inp.splitlines()):
        for j, c in enumerate(line):
            if c == "S":
                beams[(j, i)] = 1
            elif c == "^":
                splitters.add((j, i))
    max_splitter_y = max(y for _, y in splitters)
    last_y = max(y for _, y in beams.keys())
    while max_splitter_y >= last_y:
        new_beams: dict[tuple[int, int], int] = {}
        for (cx, cy), path_count in beams.items():
            if (cx, cy) in splitters:
                new_beams[(cx - 1, cy + 1)] = (
                    new_beams.get((cx - 1, cy + 1), 0) + path_count
                )
                new_beams[(cx + 1, cy + 1)] = (
                    new_beams.get((cx + 1, cy + 1), 0) + path_count
                )
            else:
                new_beams[(cx, cy + 1)] = new_beams.get((cx, cy + 1), 0) + path_count
        beams = new_beams
        last_y = next(y for _, y in beams.keys())
    return sum(beams.values())
