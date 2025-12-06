"""🎄 Solution for Day 6 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 06.py
"""

import math

inp = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


part1_asserts = [
    (inp, 4277556),
]
part2_asserts = [
    (inp, 3263827),
]


def part1(inp: str) -> str | int | None:
    numbers = {}
    operations = []
    for i, line in enumerate(inp.splitlines()[:-1]):
        for j, token in enumerate(line.split()):
            numbers[i, j] = int(token)
    for j, token in enumerate(inp.splitlines()[-1].split()):
        operations.append(token)

    res = 0
    len_inp = len(inp.splitlines()) - 1
    for j, op in enumerate(operations):
        col_numbers = [numbers[i, j] for i in range(len_inp)]
        res += sum(col_numbers) if op == "+" else math.prod(col_numbers)
    return res


def part2(inp: str) -> str | int | None:
    lines = inp.splitlines()
    op_line = lines[-1]
    data_lines = lines[:-1]
    width = len(lines[0])

    res = 0
    to_add = []
    operation = ""

    for col in range(width):
        col_str = "".join(line[col] for line in data_lines).strip()
        op_char = op_line[col]

        if op_char != " ":
            operation = op_char

        if not col_str:
            res += sum(to_add) if operation == "+" else math.prod(to_add)
            to_add = []
        else:
            to_add.append(int(col_str))

    # Handle final group
    res += sum(to_add) if operation == "+" else math.prod(to_add)

    return res
