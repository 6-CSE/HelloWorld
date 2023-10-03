def kadanes_algorithm(arr):
    if not arr:
        return 0

    max_ending_here = max_so_far = arr[0]

    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray_sum = kadanes_algorithm(arr)
print("Maximum subarray sum:", max_subarray_sum)
