import heapq
from collections import defaultdict
# find the path that maximize the product of probabilities
N = 5
edges = [[0,1], [1,2], [0,3], [1,3], [1,4], [2,4], [3,4]]
dists = [6, 5, 1, 2, 2, 5, 1]

graph = defaultdict(list)
for i in range(len(edges)):
    graph[edges[i][0]].append((edges[i][1], dists[i]))
    graph[edges[i][1]].append((edges[i][0], dists[i]))

visited = [False for i in range(N)]
distances = [float('inf') for i in range(N)]
parent = [None for i in range(N)]
parent[0] = 0
heap = [(0, 0)]
heapq.heapify(heap)

while heap:
    dist, node = heapq.heappop(heap)
    if visited[node] == False:
        distances[node] = dist
        visited[node] = True
        for k, d in graph[node]:
            if visited[k] == False:
                new_dist = dist + d
                if new_dist < distances[k]:
                    distances[k] = new_dist
                    parent[k] = node
                    heapq.heappush(heap, (new_dist, k))
    

def retrieve_path(start, end):
    if distances[end] == float('inf'):
        return []

    path = []
    node = end
    while node != start:
        path.append(node)
        node = parent[node]
    path.append(start)
    return path[::-1]


print (distances)
print (visited)
print (parent)
print (retrieve_path(0, 4))














    
                
