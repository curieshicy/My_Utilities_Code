
def dijkstra(graph, costs, parent):
    processed = []
    def find_lowest_cost_node():
        lowest_cost = inf
        lowest_cost_node = None
        for node in costs.keys():
            if node not in processed and costs[node] < lowest_cost:
                lowest_cost = costs[node]
                lowest_cost_node = node
        return lowest_cost_node

    node = find_lowest_cost_node()
    while node: # first node is 's'
        cur_cost = costs[node]  #  0
        neighbors = graph[node] #  {'a': 6, 'b': 2}
        for n in neighbors.keys(): # 'a' and 'b'
            new_cost = cur_cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parent[n] = node
        processed.append(node)
        node = find_lowest_cost_node()

    return costs, parent

if __name__ == '__main__':
        #    ---6-->A---1--->    
    #           ^
    #  S        |         T
    #           |          
    #    ---2-->B---5--->
    inf = float('inf')
    graph = {}
    graph['s'] = {}
    graph['a'] = {}
    graph['b'] = {}
    graph['t'] = {}

    graph['s']['a'] = 6
    graph['s']['b'] = 2
    graph['b']['a'] = 3
    graph['b']['t'] = 5
    graph['a']['t'] = 1
    # how about t? t goes nowhere

    costs = {}
    costs['s'] = 0
    costs['a'] = inf
    costs['b'] = inf
    costs['t'] = inf

    parent = {}
    parent['a'] = 's'
    parent['b'] = 's'
    parent['t'] = None

    print (dijkstra(graph, costs, parent))
