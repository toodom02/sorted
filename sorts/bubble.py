def bubbleSort(array):

    sorted = False
    while not sorted:
        sorted = True

        for x in range(len(array)-1):
            if array[x] > array[x+1]:
                sorted = False
                array[x], array[x+1] = array[x+1], array[x]

            yield array
