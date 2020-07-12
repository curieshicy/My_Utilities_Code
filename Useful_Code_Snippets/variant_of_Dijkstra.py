import heapq
from collections import defaultdict
# find the path that maximize the product of probabilities
N = 5
edges = [[0,1], [1,2], [0,3], [1,3], [1,4], [2,4], [3,4]]
probs = [0.6, 0.5, 0.1, 0.2, 0.2, 0.5, 0.1]

graph = defaultdict(list)
for i in range(len(edges)):
    graph[edges[i][0]].append((edges[i][1], probs[i]))
    graph[edges[i][1]].append((edges[i][0], probs[i]))

visited = [False for i in range(N)]
distances = [float('inf') for i in range(N)]
parent = [None for i in range(N)]
parent[0] = 0
heap = [(-1, 0)]
heapq.heapify(heap)

while heap:
    prob, node = heapq.heappop(heap)
    if visited[node] == False:
        distances[node] = prob
        visited[node] = True
        for k, p in graph[node]:
            if visited[k] == False:
                new_prob = prob * p
                if new_prob < distances[k]:
                    distances[k] = new_prob
                    parent[k] = node
                    heapq.heappush(heap, (new_prob, k))

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

# positive probability
B = [-i for i in distances]
print (B)
print (parent)
print (retrieve_path(0, 4))















    
                
