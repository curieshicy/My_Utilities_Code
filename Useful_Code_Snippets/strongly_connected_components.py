from collections import defaultdict 
edges = [[0, 1], [1, 3], [1, 2], [1, 4], [4, 11], [4, 1], [2, 5], 
         [5, 6], [6, 5], [6, 2], [5, 8], [7, 8], [7, 9], [9, 7],
         [8, 9], [9, 10], [10, 11], [11, 8]]
graph = defaultdict(list)
r_graph = defaultdict(list)
for start, end in edges:
    graph[start].append(end)
    r_graph[end].append(start)

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

# find topological order on reverse graph
topo_order, pre, post, is_cycle = topo_sort(r_graph, 12, 2, dict(), dict())
topo_order = topo_order[::-1]
print (topo_order)

def traverse(graph, u, explored):
    visited[u] = True
    explored.append(u)
    for v in graph[u]:
        if visited[v] == False:
            traverse(graph, v, explored)
    return explored

n = 12
visited = [False for i in range(n)]
strong_connected_comps = defaultdict(list)

i = 1
while topo_order:
    start = topo_order.pop()
    if visited[start] == False:
        explored_vertices = traverse(graph, start, [])
        strong_connected_comps[i].extend(explored_vertices)
        i += 1

# output reverse topologically sorted SCC
print (strong_connected_comps)
