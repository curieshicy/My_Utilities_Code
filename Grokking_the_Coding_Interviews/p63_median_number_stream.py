import heapq
class my_code_MedianOfAStream:
    def __init__(self):
        self.counter = 0
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)
        
    def insert_num(self, num):
        self.counter += 1
        if self.counter % 2 == 1:
            if self.min_heap:
                if num <= self.min_heap[0]:
                    heapq.heappush(self.max_heap, -num)
                else:
                    num_from_min_heap = heapq.heappushpop(self.min_heap, num)
                    heapq.heappush(self.max_heap, -num_from_min_heap)
            else:
                heapq.heappush(self.max_heap, -num)
                
        else:
            if self.max_heap:
                if num >= -self.max_heap[0]:
                    heapq.heappush(self.min_heap, num)
                else:
                    num_from_max_heap = -heapq.heappushpop(self.max_heap, num)
                    heapq.heappush(self.min_heap, num_from_max_heap)
            else:
                heapq.heappush(self.min_heap, num)
            
    def find_median(self):
        if self.counter % 2 == 0:
            median = (heapq.heappop(self.min_heap) + heapq.heappop(self.max_heap)) / 2.0
        else:
            median = -heapq.heappop(self.max_heap)
        return median

# these are the official solution
class MedianOfAStream:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        
    def insert_num(self, num):
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
            
        if len(self.max_heap) - len(self.min_heap) > 1:
            num_from_max_heap = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -num_from_max_heap)
        
        if len(self.max_heap) - len(self.min_heap) < 0:
            num_from_min_heap = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -num_from_min_heap)
            
    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return -self.max_heap[0]

def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
