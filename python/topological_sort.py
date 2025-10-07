#Topological Sort (Kahn’s Algorithm)

from collections import deque

def topo_sort(graph):
    indegree = {u:0 for u in graph}
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    q = deque([u for u in graph if indegree[u] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    return order
