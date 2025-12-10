"""🎄 Solution for Day 10 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 10.py
"""

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

inp = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
part1_asserts = [
    (inp, 7),
]
part2_asserts = [
    (inp, 33),
]


def part1(inp: str) -> str | int | None:
    cnt = 0
    for line in inp.splitlines():
        diagram, *buttons, _ = line.split(" ")
        diagram = diagram.strip("[]")
        buttons = [tuple(map(int, b.strip("()").split(","))) for b in buttons]

        n = len(diagram)
        m = len(buttons)
        target = [1 if c == "#" else 0 for c in diagram]

        # Build augmented matrix [A|b] for Gaussian elimination over GF(2)
        matrix = []
        for i in range(n):
            row = [1 if i in b else 0 for b in buttons] + [target[i]]
            matrix.append(row)

        # Gaussian elimination over GF(2)
        pivot_cols = []
        pivot_row = 0
        for col in range(m):
            # Find pivot row
            found = None
            for row in range(pivot_row, n):
                if matrix[row][col] == 1:
                    found = row
                    break
            if found is None:
                continue
            # Swap rows
            matrix[pivot_row], matrix[found] = matrix[found], matrix[pivot_row]
            pivot_cols.append(col)
            # Eliminate other rows
            for row in range(n):
                if row != pivot_row and matrix[row][col] == 1:
                    for c in range(m + 1):
                        matrix[row][c] ^= matrix[pivot_row][c]
            pivot_row += 1

        # Find free variables (columns without pivots)
        free_cols = [c for c in range(m) if c not in pivot_cols]

        # Try all combinations of free variables to find minimum presses
        min_presses = m + 1
        for free_bits in range(1 << len(free_cols)):
            solution = [0] * m
            # Set free variables
            for i, col in enumerate(free_cols):
                solution[col] = (free_bits >> i) & 1
            # Back-substitute to find pivot variables
            for row, col in enumerate(pivot_cols):
                val = matrix[row][m]
                for c in range(col + 1, m):
                    val ^= matrix[row][c] * solution[c]
                solution[col] = val
            min_presses = min(min_presses, sum(solution))

        cnt += min_presses

    return cnt


def part2(inp: str) -> str | int | None:
    cnt = 0
    for line in inp.splitlines():
        _, *buttons, joltage = line.split(" ")
        joltage = list(map(int, joltage.strip("{}").split(",")))
        buttons = [tuple(map(int, b.strip("()").split(","))) for b in buttons]

        n_positions = len(joltage)
        n_buttons = len(buttons)

        # Build matrix A where A[i][j] = 1 if button j affects position i
        A_eq = np.zeros((n_positions, n_buttons), dtype=np.float64)
        for j, b in enumerate(buttons):
            for pos in b:
                A_eq[pos, j] = 1
        b_eq = np.array(joltage, dtype=np.float64)

        # Minimize sum of presses (all coefficients = 1)
        c = np.ones(n_buttons)

        # Use MILP (mixed-integer linear programming) for integer solutions
        constraints = LinearConstraint(A_eq, b_eq, b_eq)
        integrality = np.ones(n_buttons)  # All variables must be integers
        result = milp(
            c, constraints=constraints, integrality=integrality, bounds=Bounds(lb=0)
        )

        cnt += int(round(result.fun))

    return cnt
