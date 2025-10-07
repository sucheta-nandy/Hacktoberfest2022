# Dijkstra’s (Shortest Path with weights)

import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]: continue
        for nei, w in graph[node]:
            if d + w < dist[nei]:
                dist[nei] = d + w
                heapq.heappush(pq, (dist[nei], nei))
    return dist
