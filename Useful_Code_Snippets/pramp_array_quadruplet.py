def array_quadruplet(arr, target):

    if len(arr) < 4:
        return []
        
    arr.sort()
    
    def two_sum(nums, start, end, goal):
        res = []
        while start < end:
            if nums[start] + nums[end] == goal:
                res.append([nums[start], nums[end]])
                start += 1
                end -= 1
            elif nums[start] + nums[end] < goal:
                start += 1
            else:
                end -= 1
        return res
        
    n = len(arr)
    # [3,4,5,6,2,8] n = 6
    # [3,4,5
    #    4,5,6
    ans = set()
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            remainder = target - arr[i] - arr[j]
            pairs = two_sum(arr, j + 1, n - 1, remainder)
            if pairs:
                for x, y in pairs:
                    quadruplet = [arr[i], arr[j], x, y]
                    quadruplet.sort()
                    ans.add(tuple(quadruplet))
    ans = [list(l) for l in ans]
    return ans

arr = [1,2,3,4,5,9,19,12,12,19]
target = 40

arr1 = [2,7,4,0,9,5,1,3]
target1 = 20
print (array_quadruplet(arr1, target1))
            
    
        
        
    
            
