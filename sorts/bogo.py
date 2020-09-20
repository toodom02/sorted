import random


def bogoSort(array):
    while array != sorted(array):
        random.shuffle(array)
        yield array
    yield array
