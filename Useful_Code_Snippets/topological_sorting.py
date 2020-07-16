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
                
    # topo_sort in O(n) time
    arr_2n_size = [None for i in range(2*n + 1)]
    for vertex, post_num in post.items():
        arr_2n_size[post_num] = vertex
    topo_order = [i for i in arr_2n_size if i != None][::-1]
    
    return topo_order, pre, post, is_cycle
        
print (topo_sort(graph, 8, 1, dict(), dict()))
