def mergeSort(array, left, right):
    if right <= left:
        return
    elif left < right:
        mid = (left+right)//2
        yield from mergeSort(array, left, mid)
        yield from mergeSort(array, mid+1, right)
        yield from merge(array, left, mid, right)
        yield array


def merge(array, left, mid, right):
    new = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if array[i] < array[j]:
            new.append(array[i])
            i += 1
        else:
            new.append(array[j])
            j += 1
    if i > mid:
        while j <= right:
            new.append(array[j])
            j += 1
    else:
        while i <= mid:
            new.append(array[i])
            i += 1
    for i, val in enumerate(new):
        array[left+i] = val
        yield array
