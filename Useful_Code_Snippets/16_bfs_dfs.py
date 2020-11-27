from collections import defaultdict, deque

pairs = [[1,2], [1,3], [1,4], [2,3], [3,4], [3,5], [4,5], [5,6], [5,7]]
graph = defaultdict(list)
for start, end in pairs:
    graph[start].append(end)
    graph[end].append(start)


def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            print (node)
            for k in graph[node]:
                if k not in visited:
                    queue.append(k)
                    visited.add(k)

def dfs(graph, start, res, visited):
    if start not in visited:
        visited.add(start)
        res.append(start)
        for node in graph[start]:
            dfs(graph, node, res, visited)
    return res
    
print (dfs(graph, 1, [], set()))

    

