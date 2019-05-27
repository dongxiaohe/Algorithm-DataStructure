edges = [
    [3, 4, 2],
    [4, 3, 1],
    [2, 4, 4],
    [0, 2, 5],
    [1, 2, -3],
    [0, 3, 9],
    [0, 1, 4]
]

import collections

def bellmanFord(edges, numVertices, start):
    distances = collections.defaultdict(list)
    for i in range(numVertices): distances[i].extend([float("inf"), None])
    distances[start] = [0, None]
    times = 0
    while times < numVertices:
        for u, v, d in edges:
            if distances[v][0] > distances[u][0] + d:
                distances[v] = [distances[u][0] + d, u]
        times += 1
    total = 0
    for key in distances:
        total += distances[key][0]
        # print(distances[key][1], key, distances[key][0])
    return total

print(bellmanFord(edges, 5, 0))
#print(bellmanFord(edges, 5, 1))
