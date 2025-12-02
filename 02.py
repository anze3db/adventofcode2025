from math import log10


def num_digits(n: int) -> int:
    return int(log10(n)) + 1 if n > 0 else 1


"""🎄 Solution for Day 2 of Advent of Code 2025 🎄

Usage:

adventofcode run 02.py
"""

inp = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
part1_asserts = [
    (inp, 1227775554),
]
part2_asserts = [
    (inp, 4174379265),
]


def is_invalid(s: str) -> bool:
    n = len(s)
    if n % 2 != 0:
        return False
    half = n // 2
    return s[:half] == s[half:]


def is_invalid_part2(s: str) -> bool:
    n = len(s)
    for size in range(1, n // 2 + 1):
        if n % size == 0:
            times = n // size
            if s[:size] * times == s:
                return True
    return False


def part1(inp: str) -> str | int | None:
    cnt = 0
    for rng in inp.split(","):
        start, end = map(int, rng.split("-"))
        for id in range(start, end + 1):
            s = str(id)
            if is_invalid(s):
                cnt += id

    # return sum(
    #     [
    #         id
    #         for (start, end) in [tuple(rng.split("-")) for rng in inp.split(",")]
    #         for id in range(int(start), int(end) + 1)
    #         if id % (div := 10 ** (int(log10(id) + 1) >> 1)) == id // div
    #     ]
    # )
    return cnt


def part2(inp: str) -> str | int | None:
    cnt = 0
    for rng in inp.split(","):
        start, end = map(int, rng.split("-"))
        for id in range(start, end + 1):
            s = str(id)
            if is_invalid_part2(s):
                cnt += id
    return cnt
