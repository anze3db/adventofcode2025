"""🎄 Solution for Day 6 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 06.py
"""

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
    for j, op in enumerate(operations):
        col_numbers = [numbers[i, j] for i in range(len(inp.splitlines()) - 1)]
        if op == "+":
            result = sum(col_numbers)
        elif op == "*":
            result = 1
            for num in col_numbers:
                result *= num
        res += result
    return res


def part2(inp: str) -> str | int | None:
    grid = {}
    j = 0
    i = 0
    res = 0
    for c in inp:
        if c == "\n":
            grid[i, j] = " "
            j += 1
            i = 0
            continue
        grid[i, j] = c
        i += 1

    max_row = max(y for _, y in grid.keys())
    max_col = max(x for x, _ in grid.keys())
    to_add = []
    operation = ""
    for column in range(max_col + 1):
        col_numbers = []
        operation = grid[column, max_row] if grid[column, max_row] != " " else operation
        for row in range(max_row):
            col_numbers.append(grid[column, row])
        n = "".join(col_numbers)
        if n.strip() == "":
            if operation == "+":
                result = sum(to_add)
            elif operation == "*":
                result = 1
                for num in to_add:
                    result *= num
            to_add = []
            res += result
        else:
            to_add.append(int(n))

    return res
