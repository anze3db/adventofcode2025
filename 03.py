"""🎄 Solution for Day 3 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 03.py
"""

inp = """987654321111111
811111111111119
234234234234278
818181911112111"""
part1_asserts = [
    (inp, 357),
]
part2_asserts = [
    (inp, 3121910778619),
]


def part1(inp: str) -> str | int | None:
    count = 0
    banks = 2
    for line in inp.splitlines():
        total_joltage = 0
        for i in range(-banks, 0):
            max_joltage = max(line[: (i + 1) if i != -1 else None])
            line = line[line.index(max_joltage) + 1 :]
            total_joltage = total_joltage * 10 + int(max_joltage)
        count += total_joltage
    return count


def part2(inp: str) -> str | int | None:
    count = 0
    banks = 12
    for line in inp.splitlines():
        total_joltage = 0
        for i in range(-banks, 0):
            max_joltage = max(line[: (i + 1) if i != -1 else None])
            line = line[line.index(max_joltage) + 1 :]
            total_joltage = total_joltage * 10 + int(max_joltage)
        count += total_joltage
    return count
