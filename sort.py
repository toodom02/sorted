import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

from sorts.bubble import bubbleSort
from sorts.insertion import insertionSort
from sorts.merge import mergeSort
from sorts.quick import quickSort
from sorts.bogo import bogoSort
from sorts.stalin import stalinSort


def animate(array, *bars):
    for bar, val in zip(bars, array):
        bar.set_height(val)


# input length of array
valid = False
while not valid:

    inputLength = input("Input Number to Sort: ").lower()

    try:
        inputLength = int(inputLength)
    except:
        pass

    if isinstance(inputLength, int):
        valid = True
    elif 'quit' in inputLength or 'exit' in inputLength:
        quit()
    else:
        print("\nError: Input Not Integer\n")


# creates array heights and shuffles
array = [i for i in range(1, inputLength+1)]
random.shuffle(array)

# input sort type
valid = False
while not valid:
    inputSort = input(
        '''
Select Sort:
    1. Bubble Sort
    2. Insertion Sort
    3. Merge Sort
    4. Quick Sort
    5. Bogo Sort
    6. Stalin Sort
''').lower()

    if 'quit' in inputSort or 'exit' in inputSort:  # before quickSort else 'qui'
        quit()
    elif inputSort == '1' or 'bub' in inputSort:
        sort = bubbleSort(array)
        name = "Bubble"
        valid = True
    elif inputSort == '2' or 'insert' in inputSort:
        sort = insertionSort(array)
        name = "Insertion"
        valid = True
    elif inputSort == '3' or 'mer' in inputSort:
        sort = mergeSort(array, 0, len(array)-1)
        name = "Merge"
        valid = True
    elif inputSort == '4' or 'qui' in inputSort:
        sort = quickSort(array, 0, len(array)-1)
        name = "Quick"
        valid = True
    elif inputSort == '5' or 'bog' in inputSort:
        sort = bogoSort(array)
        name = "Bogo"
        valid = True
    elif inputSort == '6' or 'stal' in inputSort:
        sort = stalinSort(array)
        name = "Stalin"
        valid = True
    else:
        print("\nError: Input Not Recognised\n")

# removes toolbar
plt.rcParams['toolbar'] = 'None'

# initialise figure and axis
fig, ax = plt.subplots()

# disables axes
ax.axis('off')

plt.title(f"{name} Sort")
fig.canvas.set_window_title(f"{name} Sort")

# initialise bar plots
bars = ax.bar(range(inputLength), array)

ani = animation.FuncAnimation(fig, animate, fargs=bars, frames=sort, interval=1,
                              repeat=False)

# saves animation to gif
##writer = animation.PillowWriter(fps=25)
##ani.save(f'media/{name}.gif', writer=writer)

plt.show()
