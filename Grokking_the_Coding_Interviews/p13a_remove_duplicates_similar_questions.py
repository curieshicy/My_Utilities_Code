def remove_all_intances_of_keys_in_place(nums, key):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] == key and nums[j] == key:
            j -= 1
        elif nums[i] != key and nums[j] != key:
            i += 1
        elif nums[i] == key and nums[j] != key:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        else:
            j -= 1
    
    print (nums)
    

arr_1 = [3, 2, 3, 6, 3, 10, 9, 3]
arr_2 = [2, 11, 2, 2, 1]

remove_all_intances_of_keys_in_place(arr_1, 3)
remove_all_intances_of_keys_in_place(arr_2, 2)
            
