import math
class ArrayReader:
    def __init__(self, arr):
        self.arr = arr
        
    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]

def search_in_infinite_array(reader, key):
    l = 0
    h = 2**64 - 1
    while l <= h:
        m = (l + h) // 2
        if reader.get(m) == key:
            return m
            
        elif reader.get(m) > key:
            h = m - 1
            
        else:
            l = m + 1
    return -1
    
def search_in_infinite_array(reader, key):
    # find the range of indexes where key is located in
    start = 0
    end = 1
    while reader.get(end) < key:
        new_start = end + 1
        new_end = end + (end - start + 1) * 2
        start, end = new_start, new_end
        
    l = start
    h = end
    while l <= h:
        m = (l + h) // 2
        if reader.get(m) == key:
            return m
        elif reader.get(m) < key:
            l = m + 1
        else:
            h = m - 1
            
    return -1
    
def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))
main()
