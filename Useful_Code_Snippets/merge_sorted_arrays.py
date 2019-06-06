# merge sorted array using two-pointers
# scenario 1: using extra space

def merge_sorted_arry_extra_space(nums1, nums2):
    res = []
    i = j = 0
    m = len(nums1)
    n = len(nums2)
    
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

def merge_sorted_arry_in_place(nums1, nums2):
    m = len(nums1) - len(nums2)
    n = len(nums2)

    i = m - 1
    j = n - 1
    count = m + n - 1
    
    while i >=0  and j >=0:
        if nums1[i] > nums2[j]:
            nums1[count] = nums1[i]
            i -= 1
            count -= 1
        else:
            nums1[count] = nums2[j]
            j -= 1
            count -=1

    nums1[: j+1] = nums2[:j+1] 
    return nums1

# test 
nums1 = [1, 10, 100]
nums2 = [2, 5, 1000]
print (merge_sorted_arry_extra_space(nums1, nums2))

nums1 = [1, 10, 20, 30, 40, 50, 60, 0, 0]
nums2 = [-1, -5]
print (merge_sorted_arry_in_place(nums1, nums2))
