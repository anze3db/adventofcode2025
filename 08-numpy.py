"""🎄 Solution for Day 8 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 08.py
"""

import numpy as np
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial.distance import pdist

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
    jboxes = np.array([[int(x) for x in line.split(",")] for line in inp.splitlines()])

    # Get the distance of the connections-th shortest edge
    dist_sq = pdist(jboxes, metric="sqeuclidean")
    threshold = np.partition(dist_sq, connections - 1)[connections - 1]

    # Use linkage + fcluster to find clusters at that distance threshold
    # Single-linkage groups points connected by edges <= threshold
    Z = linkage(jboxes, method="single", metric="sqeuclidean")
    labels = fcluster(Z, t=threshold, criterion="distance")

    # Count cluster sizes
    _, counts = np.unique(labels, return_counts=True)
    largest_sizes = np.sort(counts)[-3:]
    return int(np.prod(largest_sizes))


def part2(inp: str) -> str | int | None:
    jboxes = np.array([[int(x) for x in line.split(",")] for line in inp.splitlines()])
    n = len(jboxes)

    # Single-linkage clustering computes MST in C (pdist + sort + union-find)
    # Z[i] = [cluster1, cluster2, distance, size]
    Z = linkage(jboxes, method="single", metric="sqeuclidean")

    # The last merge Z[n-2] connects the final two clusters
    c1, c2 = int(Z[n - 2, 0]), int(Z[n - 2, 1])

    # Track which original points are in each final cluster
    # Build membership during the linkage replay
    members: list[list[int]] = [[i] for i in range(n)]
    for i in range(n - 2):  # Stop before the last merge
        a, b = int(Z[i, 0]), int(Z[i, 1])
        members.append(members[a] + members[b])

    # Now members[c1] and members[c2] have the two final clusters (before last merge)
    # Find the edge: the pair (p1 from c1, p2 from c2) with distance == merge_dist
    pts1 = np.array(members[c1])
    pts2 = np.array(members[c2])

    # Compute distances between all pairs in the two clusters
    diffs = jboxes[pts1, np.newaxis, :] - jboxes[pts2, :]  # shape: (len1, len2, 3)
    dists = np.sum(diffs**2, axis=2)
    min_idx = np.unravel_index(np.argmin(dists), dists.shape)
    p1, p2 = pts1[min_idx[0]], pts2[min_idx[1]]

    return int(jboxes[p1][0] * jboxes[p2][0])
