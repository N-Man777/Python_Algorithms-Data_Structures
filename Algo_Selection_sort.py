def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
