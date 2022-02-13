def partition(array, start, end):
    pivot = array[start]
    low = start
    high = end

    while True:

        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):

    if start >= end:
        return

    pivot = partition(array, start, end)

    quick_sort(array, start, pivot - 1)
    quick_sort(array, pivot + 1, end)


array = [29, 99, 27, 41, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]

quick_sort(array, 0, len(array) - 1)
print(*array)
