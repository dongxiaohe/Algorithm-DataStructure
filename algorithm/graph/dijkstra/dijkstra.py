def dijkstra(times, N, K):
    routes, seen, minHeap = collections.defaultdict(list), {}, []
    for u, v, w in times:
        routes[u].append([v, w])
    heapq.heappush(minHeap, [0, K])
    while minHeap:
        time, tmpNode = heapq.heappop(minHeap)
        if tmpNode not in seen:
            seen[tmpNode] = time
            for v, w in routes[tmpNode]:
                heapq.heappush(minHeap, [time + w, v])
    return max(seen.values()) if N == len(seen) else -1
