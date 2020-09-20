def stalinSort(array):
    last = 0
    for x in range(len(array)-1):
        if array[last] > array[x+1]:
            array[x+1] = 0
            yield array
        else:
            last = x+1
    yield array
