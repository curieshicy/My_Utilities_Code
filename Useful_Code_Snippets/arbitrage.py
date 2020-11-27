import math
def abitrage(edges, n):
    new_edges = []
    for u, v, w in edges:
        new_edge = [u, v, math.log(w)]
        new_edges.append(new_edge)
    
    distances = [float('inf') for i in range(n)]
    distances[0] = 0
    
    for i in range(n - 1):
        for u, v, w in new_edges:
            distances[v] = min(distances[v], distances[u] + w)
        print (distances)
    new_distances = distances.copy()
    for u, v, w in new_edges:
        new_distances[v] = min(new_distances[v], new_distances[u] + w)
    
    print (new_distances)
    if new_distances == distances:
        return False
    
    return True
    
    
'''
'USD': 0,
'GBP': 1,
'INR': 2,
'EUR': 3
'''

edges = [[0,1,0.77], [0,2,71.71], [0,3,0.87],
         [1,0,1.30], [1,2,93.55], [1,3,1.14],
         [2,0,0.014], [2,1,0.011], [2,3,0.012],
         [3,0,1.14], [3,1,0.88], [3,2,81.95]]
         
print (abitrage(edges, 4))

