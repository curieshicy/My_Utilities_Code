from heapq import *
import heapq
class SlidingWindowMedian:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
    
    def rebalance_heaps(self):
        if len(self.max_heap) - len(self.min_heap) > 1:
            num_from_max_heap = heappop(self.max_heap)
            heappush(self.min_heap, -num_from_max_heap)
            
        if len(self.max_heap) - len(self.min_heap) < 0:
            num_from_min_heap = heappop(self.min_heap)
            heappush(self.max_heap, -num_from_min_heap)
    
    def remove_element_from_heap(self, heap, element):
        index = heap.index(element)
        heap[index] = heap[-1]
        del heap[-1]
        if index < len(heap):
            heapq._siftup(heap, index)
            heapq._siftdown(heap, 0, index)
        
    def find_sliding_window_median(self, nums, k):
        result = []
        for i in range(len(nums)):
            # add number
            if not self.max_heap or nums[i] <= -self.max_heap[0]:
                heappush(self.max_heap, -nums[i])
            else:
                heappush(self.min_heap, nums[i])
            # reblance heaps
            self.rebalance_heaps()
            # record median
            if i - k + 1 >= 0:
                if k % 2 == 0:
                    median = (-self.max_heap[0] + self.min_heap[0]) / 2.0
                else:
                    median = (-self.max_heap[0]) / 1.0
                result.append(median)
                
                element_to_remove = nums[i-k+1]
                # remove number
                if element_to_remove <= -self.max_heap[0]:
                    self.remove_element_from_heap(self.max_heap, -element_to_remove)
                else:
                    self.remove_element_from_heap(self.min_heap, element_to_remove)
                # rebalance heaps
                self.rebalance_heaps()
                
        return result

def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))
main()
