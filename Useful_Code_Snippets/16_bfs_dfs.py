from collections import defaultdict, deque

pairs = [[1,2], [1,3], [1,4], [2,3], [3,4], [3,5], [4,5], [5,6], [5,7]]
graph = defaultdict(list)
for start, end in pairs:
    graph[start].append(end)
    graph[end].append(start)
    

def dfs(graph, start, visited, res):
    visited.add(start)
    res.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, res)
    return res


def bfs(graph, start, visited, res):
    queue = deque([start])
    visited = {start}
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            res.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
    return res

print (dfs(graph, 1, set(), []))
print (bfs(graph, 1, set(), []))
    
    


    

