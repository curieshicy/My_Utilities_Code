def floyd_warshall(edges, n):
    adj_mat = [[float('inf') for i in range(n)] for j in range(n)]

    for start, end, weight in edges:
        adj_mat[start][end] = weight

    for i in range(n):
        adj_mat[i][i] = 0

    # D(i, s, t) = min(D(i-1, s, t), D(i-1, s, i) + D(i-1, i, t))
    for i in range(n):
        for s in range(n):
            for t in range(n):
                adj_mat[s][t] = min(adj_mat[s][t], adj_mat[s][i] + adj_mat[i][t])

    # check if exists a negative weighted cycle
    is_neg_cycle = False
    for i in range(n):
        if adj_mat[i][i] < 0:
            is_neg_cycle = True
            break

    for row in adj_mat:
        print (row)
    print (is_neg_cycle)
    return adj_mat, is_neg_cycle

def bellman_ford(edges, n, start):
    distances = [float('inf') for i in range(n)]
    distances[start] = 0

    for i in range(n-1):
        for u, v, w in edges:
            distances[v] = min(distances[v], distances[u] + w)

    # check if cycle exists
    new_distances = distances.copy()
    for u, v, w in edges:
       new_distances[v] = min(new_distances[v], new_distances[u] + w)

    is_neg_cycle = False
    if new_distances != distances:
        is_neg_cycle = True

    print (distances, new_distances, is_neg_cycle)
    return distances, is_neg_cycle

if __name__ == '__main__':
    # directed graph
    # edge -- [node 1, node 2, weight]
    edges_1 = [[0, 3, -1],
               [0, 1, 5],
               [1, 3, 3],
               [2, 0, 1],
               [1, 2, -7],
               [2, 4, 4],
               [4, 1, 6]]

    edges_2 = [[0, 1, 6],
               [1, 0, 6],
               [0, 3, 1],
               [3, 0, 1],
               [1, 3, 2],
               [3, 1, 2],
               [3, 4, 1],
               [4, 3, 1],
               [4, 1, 2],
               [1, 4, 2],
               [1, 2, 5],
               [2, 1, 5],
               [4, 2, 5],
               [2, 4, 5]]

    floyd_warshall(edges_2, 5)
    bellman_ford(edges_2, 5, 0)
    bellman_ford(edges_2, 5, 1)
    bellman_ford(edges_2, 5, 2)
    bellman_ford(edges_2, 5, 3)
    bellman_ford(edges_2, 5, 4)


    
