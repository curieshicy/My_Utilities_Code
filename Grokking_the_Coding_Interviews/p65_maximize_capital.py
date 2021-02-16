import bisect
import heapq
def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    cur_cap = initialCapital
    cap_pro = [(c, p) for c, p in zip(capital, profits)]
    
    cap_pro.sort(key = lambda t: t[0])
    caps_sorted = [i[0] for i in cap_pro]
    pros = [(-pro[1], idx) for idx, pro in enumerate(cap_pro)]
    
    while numberOfProjects:
        index = bisect.bisect_left(caps_sorted, cur_cap)
        heap = pros[:index + 1]
        heapq.heapify(heap)
        neg_profit, _ = heap[0]
        cur_cap -= neg_profit
        numberOfProjects -= 1
        
    return cur_cap

def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):  
    min_capital_heap = []
    max_profit_heap = []
    cur_capital = initialCapital
    
    n = len(capital)
    for i in range(n):
        heapq.heappush(min_capital_heap, (capital[i], i))
    
    for _ in range(numberOfProjects):
        while min_capital_heap and min_capital_heap[0][0] <= cur_capital:
            capital, idx = heapq.heappop(min_capital_heap)
            heapq.heappush(max_profit_heap, -profits[idx])
        
        if not max_profit_heap:
            break
            
        cur_capital -= max_profit_heap[0]
        
    return cur_capital
    
    
def main():
    print("Maximum capital: " + str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " + str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
