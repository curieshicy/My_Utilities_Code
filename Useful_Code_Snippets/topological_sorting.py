from collections import defaultdict
edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 4]]
graph = defaultdict(list)
for start, end in edges:
    graph[start].append(end)

def topo_sort(graph, n, pre, post):
    def explore(u):
        nonlocal clock
        pre[u] = clock
        clock += 1
        visited[u] = True
        for v in graph[u]:
            if visited[v] == False:
                explore(v)
        post[u] = clock
        clock += 1
        
    clock = 1
    visited = [False for i in range(n)]
    for node in range(n):
        if visited[node] == False:
            explore(node)

    # detect back edge == detect cycle
    is_cycle = False
    for start in graph.keys():
        for end in graph[start]:
            if post[start] < post[end]:
                is_cycle = True
                break
    # topo_sort      
    sorted_keys = sorted(post.keys(), key = post.get, reverse = True)
    return sorted_keys, pre, post, is_cycle
        

print (topo_sort(graph, 8, dict(), dict()))



