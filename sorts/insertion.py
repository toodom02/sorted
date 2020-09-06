def insertionSort(array):

    for i in range(1, len(array)):
        currentVal = array[i]
        position = i

        while position > 0 and array[position-1] > currentVal:
            array[position] = array[position-1]
            position -= 1
            yield array

        array[position] = currentVal

        yield array
