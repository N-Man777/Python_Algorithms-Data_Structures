def binary_search(array, target):
    i = 0
    j = len(array)-1
    while i <= j:
        m = (i + j) // 2
        if array[m] == target:
            return m
        elif target > array[m]:
            i = m + 1
        else:
            j = m - 1
    else:
        return False