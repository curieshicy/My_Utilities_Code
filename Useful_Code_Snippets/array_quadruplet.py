def find_array_quadruplet(arr, s):
    # corner case
    if len(arr) < 4:
        return []
    if len(arr) == 4:
        if sum(arr) == s:
            return sorted(arr)
        return []
    
    arr.sort()
    def two_sum(nums, start, end, target):
        res = set()
        while start < end:
            summation = nums[start] + nums[end]
            if summation == target:
                res.add((nums[start], nums[end]))
                start += 1
                end -= 1
            elif summation < target:
                start += 1
            else:
                end -= 1
        return res      

    def three_sum(nums, target):
        res = set()
        for i in range(len(nums) - 2):
          doublets = two_sum(nums, i + 1, len(nums) - 1, target - nums[i])
          if doublets:
              for doublet in doublets:
                res.add((nums[i], doublet[0], doublet[1]))
        return res

    res = set()
    for i in range(len(arr) - 3):
        triplets = three_sum(arr[i + 1:], s - arr[i])
        if triplets:
            for triplet in triplets:
                res.add((arr[i], triplet[0], triplet[1], triplet[2]))
    if not res:
        return []
    res_sort = [sorted(i) for i in res]
    res_sort.sort()
    return res_sort[0]

def find_array_quadruplet_1(arr, s):
    if len(arr) < 4:
        return []

    def two_sum(nums, start, end, target):
        while start < end:
          summation = nums[start] + nums[end]
          if summation == target:
            return (start, end)
          elif summation < target:
            start +=1 
          else:
            end -= 1
        return (-1, -1)

    arr.sort()
    start = 0
    end = len(arr) - 1
    while start < end:
        summation = arr[start] + arr[end]
        if summation < s:
            middle_indexes = two_sum(arr, start + 1, end - 1, s - summation)
            if middle_indexes != (-1, -1):
                return [arr[start], arr[middle_indexes[0]], arr[middle_indexes[1]], arr[end]]

        if summation > s:
            end -= 1
        else:
            start += 1
    return []

def find_array_quadruplet_2(arr, s):
    if len(arr) < 4:
        return []

    arr.sort()
    for i in range(len(arr) - 3):
        for j in range(i + 1, len(arr) - 2):
            r = s - arr[i] - arr[j]
            l = j + 1
            h = len(arr) - 1
            while l < h:
                if arr[l] + arr[h] < r:
                    l += 1
                elif arr[l] + arr[h] > r:
                    h -=1
                else:
                    return [arr[i], arr[j], arr[l], arr[h]]

    return []
            

print(find_array_quadruplet([2, 7, 4, 0, 9, 5, 1, 3], 20))
print(find_array_quadruplet([4, 4, 4, 2], 16))
print (find_array_quadruplet([1,2,3,4,5,9,19,12,12,19], 40))

print(find_array_quadruplet_1([2, 7, 4, 0, 9, 5, 1, 3], 20))
print(find_array_quadruplet_1([4, 4, 4, 2], 16))
print (find_array_quadruplet_1([1,2,3,4,5,9,19,12,12,19], 40))

print(find_array_quadruplet_2([2, 7, 4, 0, 9, 5, 1, 3], 20))
print(find_array_quadruplet_2([4, 4, 4, 2], 16))
print (find_array_quadruplet_2([1,2,3,4,5,9,19,12,12,19], 40))
