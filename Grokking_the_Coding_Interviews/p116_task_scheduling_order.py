from collections import defaultdict, deque
def find_order(tasks, prerequisites):
    sortedOrder = []
    indegrees = defaultdict(int)
    graph = defaultdict(list)
    for u, v in prerequisites:
        indegrees[v] += 1
        graph[u].append(v)
        
    queue = deque()
    for i in range(tasks):
        if indegrees[i] == 0:
            queue.append(i)
            
    while queue:
        node = queue.popleft()
        sortedOrder.append(node)
        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
                
    if len(sortedOrder) != tasks:
        return []
    return sortedOrder


def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " + str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))
main()
