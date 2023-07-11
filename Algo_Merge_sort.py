def merge(left_array, right_array):
    l, r = len(left_array), len(right_array)
    merged_array = [None]*(l+r)
    i = j = s = 0
    while i < l and j < r:
        if left_array[i] < right_array[j]:
            merged_array[s] = left_array[i]
            s += 1
            i += 1
        else:
            merged_array[s] = right_array[j]
            s += 1
            j += 1
    else:
        if i == l:
            merged_array[s:] = right_array[j:]
        else:
            merged_array[s:] = left_array[i:]
    return merged_array

def merge_sort(array):
    n = len(array)
    if n == 1:
        return array
    left_array = merge_sort(array[:n//2])
    right_array = merge_sort(array[n//2:])
    sorted_array = merge(left_array, right_array)
    return sorted_array