from collections import deque, defaultdict
def find_trees(num_nodes, edges):
    if num_nodes <= 0:
        return []
    if num_nodes == 1:
        return [0]
        
    graph = defaultdict(list)
    indegrees = defaultdict(int)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        indegrees[u] += 1
        indegrees[v] += 1
        
    leaves = deque()
    for key in indegrees:
        if indegrees[key] == 1:
            leaves.append(key)
        
    total_nodes = num_nodes
    removed_nodes = set()
    while total_nodes > 2:
        total_nodes -= len(leaves)
        for _ in range(len(leaves)):
            node = leaves.popleft()
            removed_nodes.add(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 1:
                    leaves.append(neighbor)
    return list(set(indegrees.keys()) - removed_nodes)


def main():
  print("Roots of MHTs: " + str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
  print("Roots of MHTs: " + str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
  print("Roots of MHTs: " + str(find_trees(4, [[0, 1], [1, 2], [1, 3]])))


main()
