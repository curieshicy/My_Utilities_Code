from collections import defaultdict, deque
def topological_sort(vertices, edges):
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder
        
    indegrees = defaultdict(int)
    graph = defaultdict(list)
    for u, v in edges:
        indegrees[v] += 1
        graph[u].append(v)
        
    queue = deque()
    for i in range(vertices):
        if indegrees[i] == 0:
            queue.append(i)
            
    while queue:
        node = queue.popleft()
        sortedOrder.append(node)
        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
    
    if len(sortedOrder) != vertices:
        return []
    return sortedOrder


def main():
    print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
