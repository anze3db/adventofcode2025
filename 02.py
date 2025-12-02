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


def part1(inp: str) -> str | int | None:
    def generate_invalid_numbers(start: int, end: int):
        start_digits = len(str(start))
        end_digits = len(str(end))

        for num_d in range(start_digits, end_digits + 1):
            if num_d % 2 != 0:
                continue
            half = num_d // 2
            # Generate all possible first halves
            min_half = max(10 ** (half - 1), start // (10**half))
            max_half = min(10**half, end // (10**half) + 1)
            for first_half in range(min_half, max_half):
                s = str(first_half)
                invalid_num = int(s + s)
                if start <= invalid_num <= end:
                    yield invalid_num

    return sum(
        sum(generate_invalid_numbers(*map(int, rng.split("-"))))
        for rng in inp.split(",")
    )


def part2(inp: str) -> str | int | None:
    def generate_invalid_numbers(start: int, end: int):
        start_digits = len(str(start))
        end_digits = len(str(end))

        seen = set()  # Avoid duplicates (e.g., 1111 can be "1"*4 or "11"*2)

        for num_d in range(start_digits, end_digits + 1):
            for pattern_size in range(1, num_d // 2 + 1):
                if num_d % pattern_size != 0:
                    continue
                times = num_d // pattern_size
                if times < 2:
                    continue

                min_pattern = max(
                    10 ** (pattern_size - 1),
                    start // (10 ** (pattern_size * (times - 1))),
                )
                max_pattern = min(
                    10**pattern_size, end // (10 ** (pattern_size * (times - 1))) + 1
                )

                for pattern in range(min_pattern, max_pattern):
                    s = str(pattern)
                    invalid_num = int(s * times)
                    if start <= invalid_num <= end and invalid_num not in seen:
                        seen.add(invalid_num)
                        yield invalid_num

    return sum(
        sum(generate_invalid_numbers(*map(int, rng.split("-"))))
        for rng in inp.split(",")
    )
