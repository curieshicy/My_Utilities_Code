from collections import defaultdict
edges = [[1, 0], [1, 2], [2, 5], [0, 3], [3, 4], [3, 7], [4, 6]]
graph = defaultdict(list)
for start, end in edges:
    graph[start].append(end)

def topo_sort(graph, n, start, pre, post):
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
    vertices = [start] + list(set(range(n)) - {start})
    for vertex in vertices:
        if visited[vertex] == False:
            explore(vertex)

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
        

print (topo_sort(graph, 8, 1, dict(), dict()))
