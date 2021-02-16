def merge(intervals_a, intervals_b):
    result = []
    # find how b intersects a
    for interval_b in intervals_b:
        x_b, y_b = interval_b
        for interval_a in intervals_a:
            x_a, y_a = interval_a
            if y_a < x_b:
                continue
            if x_a <= y_b: # the opposite is x_a > y_b ---> no overlap
                result.append([max(x_a, x_b), min(y_a, y_b)])
    return result

def merge_optimal(intervals_a, intervals_b):
    result = []
    i = 0
    j = 0
    start = 0
    end = 1
    
    while i < len(intervals_a) and j < len(intervals_b):
        is_a_overlap_b = intervals_a[i][start] >= intervals_b[j][start] and intervals_a[i][start] <= intervals_b[j][end]
        is_b_overlap_a = intervals_b[j][start] >= intervals_a[i][start] and intervals_b[j][start] <= intervals_a[i][end]
        if is_a_overlap_b or is_b_overlap_a:
            result.append([max(intervals_a[i][start], intervals_b[j][start]),\
                           min(intervals_a[i][end], intervals_b[j][end])])
                           
        if intervals_a[i][end] <= intervals_b[j][end]:
            i += 1
        else:
            j += 1
            
    return result
    
def main():
    print("Intervals Intersection: " + str(merge_optimal([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge_optimal([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
