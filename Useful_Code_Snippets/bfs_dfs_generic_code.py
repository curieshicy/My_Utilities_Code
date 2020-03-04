from collections import OrderedDict, deque

def dfs(graph, start, visited = OrderedDict()):
    visited[start] = 1
    
    for node in graph[start]:
        if node not in visited:
            visited[node] = 1
            dfs(graph, node, visited)

    return visited


def bfs(graph, start, visited = OrderedDict()):
    visited[start] = 1
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if i not in visited:
                visited[i] = 1
                queue.append(i)

    return visited

if __name__ == '__main__':

    #         A
    #      B     C
    #    D   E  F   G   

    graph_1 = {
               'A': ['B', 'C'],
               'B': ['D', 'E'],
               'C': ['F', 'G'],
               'D': [],
               'E': [],
               'F': [],
               'G': []
               }

    start_node = 'A'
    visited_dict_1 = OrderedDict()
    visited_dict_2 = OrderedDict()
    
    visited_dfs = list(dfs(graph_1, start_node, visited_dict_1).keys())
    visited_bfs = list(bfs(graph_1, start_node, visited_dict_2).keys())

    print (visited_dfs)
    print (visited_bfs)
