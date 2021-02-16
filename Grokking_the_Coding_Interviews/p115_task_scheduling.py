from collections import defaultdict, deque
def is_scheduling_possible(tasks, prerequisites):
    indegrees = defaultdict(int)
    graph = defaultdict(list)
    for u, v in prerequisites:
        indegrees[v] += 1
        graph[u].append(v)
        
    queue = deque()
    for i in range(tasks):
        if indegrees[i] == 0:
            queue.append(i)
            
    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
                
    return len(topo_order) == tasks


def main():
    print("Is scheduling possible: " + str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " + str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " + str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()
