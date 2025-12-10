"""🎄 Solution for Day 10 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 10.py
"""

from itertools import product

import z3

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
        target = [1 if c == "#" else 0 for c in diagram]
        button_masks = []
        for b in buttons:
            mask = [0] * n
            for idx in b:
                mask[idx] = 1
            button_masks.append(mask)

        min_presses = 0
        for presses in product(range(2), repeat=len(buttons)):
            state = [0] * n
            for b_idx, press in enumerate(presses):
                if press == 1:
                    for i in range(n):
                        state[i] ^= button_masks[b_idx][i]
            if state == target:
                total_presses = sum(presses)
                if min_presses == 0 or total_presses < min_presses:
                    min_presses = total_presses
        cnt += min_presses

    return cnt


def part2(inp: str) -> str | int | None:
    cnt = 0
    for line in inp.splitlines():
        _, *buttons, joltage = line.split(" ")
        joltage = tuple(map(int, joltage.strip("{}").split(",")))
        buttons = [tuple(map(int, b.strip("()").split(","))) for b in buttons]

        s = z3.Optimize()
        presses = [z3.Int(f"b{i}") for i in range(len(buttons))]
        for i in range(len(buttons)):
            s.add(presses[i] >= 0)
        for i in range(len(joltage)):
            s.add(
                sum(presses[j] for j, b in enumerate(buttons) if i in b) == joltage[i]
            )
        s.minimize(sum(presses))
        if s.check() != z3.sat:
            raise ValueError("No solution found")
        min_presses = sum(
            s.model().evaluate(presses[i]).as_long() for i in range(len(buttons))
        )
        cnt += min_presses

    return cnt
