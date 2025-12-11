"""🎄 Solution for Day 11 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 11.py
"""

from functools import lru_cache

inp = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""
part1_asserts = [
    (inp, 5),
]
part2_asserts = [
    (
        """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out""",
        2,
    ),
]


def part1(inp: str) -> str | int | None:
    start = "you"
    target = "out"

    edges = {}
    for line in inp.splitlines():
        node, children = line.split(": ")
        edges[node] = children.split(" ")

    def dfs(node):
        if node == target:
            return 1
        return sum(dfs(child) for child in edges.get(node, []))

    return dfs(start)


def part2(inp: str) -> str | int | None:
    start = "svr"
    target = "out"

    edges = {}
    for line in inp.splitlines():
        node, children = line.split(": ")
        edges[node] = children.split(" ")

    @lru_cache(maxsize=None)
    def dfs(node, seen_dac, seen_fft):
        if node == target:
            return int(seen_dac and seen_fft)
        return sum(
            dfs(child, seen_dac or child == "dac", seen_fft or child == "fft")
            for child in edges.get(node, [])
        )

    return dfs(start, False, False)
