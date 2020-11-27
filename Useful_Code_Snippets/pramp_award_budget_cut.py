def find_grants_cap(grants, newBudget):
    n = len(grants)
    grants.sort()
    prefix_sum = [grants[0]]
    for i in range(1, n):
        prefix_sum.append(prefix_sum[-1] + grants[i])
        
    max_cap = float('-inf')
    # not cut first grant
    cap = newBudget / n
    if cap < grants[0]:
        max_cap = max(max_cap, cap)
    
    for i in range(n - 1):
        cap = (newBudget - prefix_sum[i]) / (n - i - 1)
        if grants[i] <= cap <= grants[i+1]:
            max_cap = max(max_cap, cap)
                
    return max_cap
    

arr = [14,15,16,17,18,19]
b1 = 97
b2 = 98
b3 = 99


print (find_grants_cap(arr, b1))
print (find_grants_cap(arr, b2))
print (find_grants_cap(arr, b3))

