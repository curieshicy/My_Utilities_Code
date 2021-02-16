import heapq
from collections import defaultdict, deque
def rearrange_string(str):
    d = defaultdict(int)
    for ch in str:
        d[ch] += 1
    
    max_heap = []
    for ch, freq in d.items():
        heapq.heappush(max_heap, (-freq, ch))
        
    prev_char, prev_freq = None, 0
    result = []
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        if prev_char and prev_freq < 0:
            heapq.heappush(max_heap, (prev_freq, prev_char))
            
        result.append(char)
        prev_char = char
        prev_freq = freq + 1
    
    if len(result) < len(str):
        return ""
    
    return ''.join(result)

def rearrange_string(str):    
    d = defaultdict(int)
    for ch in str:
        d[ch] += 1
    
    max_heap = []
    for ch, freq in d.items():
        heapq.heappush(max_heap, (-freq, ch))
        
    queue = deque()
    k = 2
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
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))
    print("Rearranged string:  " + rearrange_string("abc"))

main()
