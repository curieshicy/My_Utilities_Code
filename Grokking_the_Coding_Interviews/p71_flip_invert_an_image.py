def flip_and_invert_image(matrix):
    def flip_an_arr(arr):
        n = len(arr)
        i = 0
        j = n - 1
        while i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
    for row in matrix:
        flip_an_arr(row)
        
    R, C = len(matrix), len(matrix[0])
    for r in range(R):
        for c in range(C):
            matrix[r][c] ^= 1
    return matrix

def main():
    print(flip_and_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
    print(flip_and_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

main()
