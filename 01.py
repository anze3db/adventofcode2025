"""🎄 Solution for Day 1 of Advent of Code 2025 🎄

Usage:

adventofcode run 01.py
"""

inp = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
inp2 = """L50
R50
L50"""
part1_asserts = [
    (inp, 3),
]
part2_asserts = [
    (inp, 6),
    (inp2, 2),
    ("R1000", 10),
]


def part1(inp: str) -> str | int | None:
    current = 50
    cnt = 0
    for line in inp.splitlines():
        direction, value = line[0], int(line[1:])
        if direction == "R":
            current += value
        else:
            current -= value
        current = current % 100
        if current == 0:
            cnt += 1
    return cnt


def part2(inp: str) -> str | int | None:
    current = 50
    cnt = 0
    for line in inp.splitlines():
        direction, value = line[0], int(line[1:])
        if direction == "R":
            new = current + value
        else:
            new = current - value

        if new == 0:
            cnt += 1
        elif new < 0:
            cnt += (-new) // 100
            if current != 0:
                cnt += 1
        else:
            cnt += new // 100

        current = new % 100

    return cnt
