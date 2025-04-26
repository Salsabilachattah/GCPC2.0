from heapq import heappop, heappush

def dijkstra(graph, source):
    n = len(graph)
    dist = [-1] * n
    dist[source-1] = 0
    heap = [(0, source)]

    while heap:
        d, u = heappop(heap)
        if d > dist[u-1] :
            continue
        for v, w in graph[u-1]:
            if dist[u-1] + w < dist[v-1]:
                dist[v-1] = dist[u-1] + w
                heappush(heap, (dist[v-1], v))

    return dist

n = int(input())
m = int(input())

graph = [[] for _ in range(n)]    

for i in range(m):                
    x, y, d = map(int, input().split())
    if not i :
        source = x
    graph[x-1].append((y, d))  
    graph[y-1].append((x, d))  

distances = dijkstra(graph, source)

for d in distances:
    print(d)


