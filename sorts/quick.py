def quickSort(array, low, high):
    if low >= high:
        return

    pivot = array[high]
    count = low

    for i in range(low, high):
        if array[i] < pivot:
            array[i], array[count] = array[count], array[i]
            count += 1
        yield array

    array[high], array[count] = array[count], array[high]

    yield array
    yield from quickSort(array, low, count - 1)
    yield from quickSort(array, count + 1, high)
