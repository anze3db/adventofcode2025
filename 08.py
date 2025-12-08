"""🎄 Solution for Day 8 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 08.py
"""

inp = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
part1_asserts = [
    (inp, 40),
]
part2_asserts = [
    (inp, 25272),
]


def part1(inp: str) -> str | int | None:
    connections = 10 if len(inp.splitlines()) < 30 else 1000
    jboxes = [tuple(int(x) for x in line.split(",")) for line in inp.splitlines()]
    n = len(jboxes)

    all_edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = sum((a - b) ** 2 for a, b in zip(jboxes[i], jboxes[j])) ** 0.5
            all_edges.append((dist, i, j))
    all_edges = sorted(all_edges)

    # Union-Find with path compression for efficient circuit merging
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py

    made_connections = 0
    for _, i, j in all_edges:
        if made_connections >= connections:
            break
        union(i, j)
        made_connections += 1

    circuit_sizes: dict[int, int] = {}
    for i in range(n):
        root = find(i)
        circuit_sizes[root] = circuit_sizes.get(root, 0) + 1
    largest_sizes = sorted(circuit_sizes.values(), reverse=True)[:3]
    product = 1
    for size in largest_sizes:
        product *= size
    return product


def part2(inp: str) -> str | int | None:
    jboxes = [tuple(int(x) for x in line.split(",")) for line in inp.splitlines()]
    n = len(jboxes)

    all_edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = sum((a - b) ** 2 for a, b in zip(jboxes[i], jboxes[j])) ** 0.5
            all_edges.append((dist, i, j))
    all_edges = sorted(all_edges)

    parent = list(range(n))
    num_circuits = n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(num_circuits, x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            num_circuits -= 1
            return num_circuits, True
        return num_circuits, False

    last_connection = (-1, -1)
    for dist, i, j in all_edges:
        if num_circuits == 1:
            break
        num_circuits, merged = union(num_circuits, i, j)
        if merged:
            last_connection = (i, j)

    box1, box2 = jboxes[last_connection[0]], jboxes[last_connection[1]]
    return box1[0] * box2[0]
