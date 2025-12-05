"""🎄 Solution for Day 5 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 05.py
"""

from bisect import bisect_right

inp = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
part1_asserts = [
    (inp, 3),
]
part2_asserts = [
    (inp, 14),
]


def part1(inp: str) -> str | int | None:
    ranges, ids = inp.split("\n\n")
    r = []
    for line in ranges.splitlines():
        a, b = map(int, line.split("-"))
        r.append((a, b))

    r.sort()
    merged = []
    for a, b in r:
        if merged and a <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else:
            merged.append((a, b))

    starts = [a for a, _ in merged]
    cnt = 0
    for number in map(int, ids.splitlines()):
        idx = bisect_right(starts, number) - 1
        if idx == -1:
            continue
        start, end = merged[idx]
        if start <= number <= end:
            cnt += 1
    return cnt


def part2(inp: str) -> str | int | None:
    ranges, _ = inp.split("\n\n")
    r = []
    cnt = 0

    for line in ranges.splitlines():
        a, b = map(int, line.split("-"))
        r.append((a, b))

    r.sort()
    current_end = -1
    for a, b in r:
        if b <= current_end:
            continue
        if a > current_end + 1:
            cnt += b - a + 1
            current_end = b
        else:
            cnt += b - current_end
            current_end = b
    return cnt
