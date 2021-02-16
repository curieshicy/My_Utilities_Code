import heapq
from collections import OrderedDict, defaultdict
def sort_character_by_frequency(str):
    od = OrderedDict()
    for ch in str:
        if ch in od:
            od[ch] += 1
        else:
            od[ch] = 1
            
    ans = ''
    freq_ch = [(freq, ch) for ch, freq in od.items()]
    freq_ch.sort(key = lambda t: t[0], reverse = True)
    for freq, ch in freq_ch:
        ans += ch * freq
        
    return ans
        
def sort_character_by_frequency(str):
    d = defaultdict(int)
    for ch in str:
        d[ch] += 1
        
    max_heap = []
    for ch, freq in d.items():
        heapq.heappush(max_heap, (-freq, ch))
        
    ans = ''
    while max_heap:
        freq, ch = heapq.heappop(max_heap)
        ans += ch * (-freq)
        
    return ans

def main():
    print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()
