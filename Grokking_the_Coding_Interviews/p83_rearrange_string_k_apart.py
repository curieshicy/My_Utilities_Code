import heapq
from collections import defaultdict, deque

def reorganize_string(str, k):
    d = defaultdict(int)
    for ch in str:
        d[ch] += 1
    
    max_heap = []
    for ch, freq in d.items():
        heapq.heappush(max_heap, (-freq, ch))
        
    queue = deque()
    result = []
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        result.append(char)
        
        queue.append((freq + 1, char))
        if len(queue) == k:
            freq, char = queue.popleft()
            if freq < 0:
                heapq.heappush(max_heap, (freq, char))
                
    if len(result) < len(str):
        return ""
    return "".join(result)

def main():
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))
    print("Reorganized string: " + reorganize_string("aaabcc", 3))


main()
