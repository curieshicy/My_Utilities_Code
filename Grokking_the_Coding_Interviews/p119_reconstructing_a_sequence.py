from collections import defaultdict, deque
def can_construct(originalSeq, sequences):
    topo_order = []
    indegrees = defaultdict(int)
    graph = defaultdict(list)
    edges = set()
    unique_nums = set()
    for seq in sequences:
        n = len(seq)
        if n < 2:
            continue
        for i in range(1, n):
            edges.add((seq[i-1], seq[i]))
            unique_nums.add(seq[i-1])
            unique_nums.add(seq[i])
    
    if len(unique_nums) != len(originalSeq):
        return False
        
    for u, v in edges:
        indegrees[v] += 1
        graph[u].append(v)
    
    queue = deque()
    for num in unique_nums:
        if indegrees[num] == 0:
            queue.append(num)
    
    while queue:
        if len(queue) != 1:
            return False
        if originalSeq[len(topo_order)] != queue[0]:
            return False
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
    return topo_order == originalSeq


def main():
    print("Can construct: " + str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " + str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " + str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))
main()
