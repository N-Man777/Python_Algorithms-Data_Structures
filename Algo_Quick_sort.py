import random

def quick_sort(arr, l, r):
    if r <= l:
        return
    splitter = random.randint(l, r)
    arr[l], arr[splitter] = arr[splitter], arr[l]
    i = j = l + 1
    while i <= r:
        if arr[l] > arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1
    else:
        arr[l], arr[j-1] = arr[j-1], arr[l]
    quick_sort(arr, l, j-2)
    quick_sort(arr, j, r)