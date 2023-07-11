import random

def merge_count_inv(left_array, right_array):
    l, r = len(left_array), len(right_array)
    inversion = 0
    merged_array = [None]*(l+r)
    i = j = s = 0
    while i < l and j < r:
        if left_array[i] <= right_array[j]:
            merged_array[s] = left_array[i]
            s += 1
            i += 1
        else:
            merged_array[s] = right_array[j]
            inversion += (l-i)
            s += 1
            j += 1
    else:
        if i == l:
            merged_array[s:] = right_array[j:]
        else:
            merged_array[s:] = left_array[i:]
    return merged_array, inversion



def inversion_count(array):
    n = len(array)
    if n == 1:
        return array, 0
    left_array, left_inversion = inversion_count(array[:n//2])
    right_array, right_inversion = inversion_count(array[n//2:])
    sorted_array, current_inversion = merge_count_inv(left_array, right_array)
    return sorted_array, left_inversion + right_inversion + current_inversion

n=5
for i in range(n):
    print(f"{i} ITERATION")
    arr = [random.randint(0, 11) for _ in range(n)]
    print(f"ARRAY: {arr}")
    sorted_arr, inversions = inversion_count(arr)
    print(f"SORTED ARRAY: {sorted_arr}, NUMBER OF INVERSIONS: {inversions}", end="\n\n")
    

