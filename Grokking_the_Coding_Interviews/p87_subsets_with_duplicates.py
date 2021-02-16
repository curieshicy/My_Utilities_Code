def find_subsets(nums):
    nums.sort()
    subsets = []
    start_idx = 0
    end_idx = 0
    subsets.append([])
    
    for i in range(len(nums)):
        start_idx = 0
        
        if i > 0 and nums[i] == nums[i-1]:
            start_idx = end_idx + 1
            
        end_idx = len(subsets) - 1
        
        for j in range(start_idx, end_idx + 1):
            subsets.append(subsets[j] + [nums[i]])

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))
main()
