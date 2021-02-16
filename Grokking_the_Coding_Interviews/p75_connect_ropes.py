import heapq
def minimum_cost_to_connect_ropes(ropeLengths):
    heap = []
    for length in ropeLengths:
        heapq.heappush(heap, length)
        
    cost = 0
    while len(heap) > 1:
        cost_1 = heapq.heappop(heap)
        cost_2 = heapq.heappop(heap)
        heapq.heappush(heap, cost_1 + cost_2)
        cost += (cost_1 + cost_2)
    
    return cost


def main():
    print("Minimum cost to connect ropes: " + str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " + str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " + str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))

main()
