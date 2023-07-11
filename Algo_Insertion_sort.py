def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0:
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1