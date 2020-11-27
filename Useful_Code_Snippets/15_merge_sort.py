def merge_lists(l1, l2):
    res = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
            
    res += l1[i:]
    res += l2[j:]
        
    return res
    
def mergeSortHelper(nums1, nums2):
    i = j = 0
    m = len(nums1)
    n = len(nums2)
    res = []
    
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1

    while i < m:
        res.append(nums1[i])
        i += 1

    while j < n:
        res.append(nums2[j])
        j += 1

    return res

def merge_sort(arr):
    if len(arr) < 2:
        return arr
        
    mid_idx = len(arr) // 2
    first_half = arr[:mid_idx]
    second_half = arr[mid_idx:]
    return merge_lists(merge_sort(first_half), merge_sort(second_half))
    

print (merge_sort([2,3,4,1,-1]))
    
    
