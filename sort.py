import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

from sorts.bubble import bubbleSort
from sorts.insertion import insertionSort


def animate(array, *bars):
    for bar, val in zip(bars, array):
        bar.set_height(val)


# creates array heights and shuffles
array = [i for i in range(1, 51)]
random.shuffle(array)

inputSort = input("Select Sort:\n1. Bubble Sort\n2. Insertion Sort\n")

if inputSort == '1':
    sort = bubbleSort(array)
    name = "Bubble"
elif inputSort == '2':
    sort = insertionSort(array)
    name = "Insertion"

# removes toolbar
plt.rcParams['toolbar'] = 'None'

# initialise figure and axis
fig, ax = plt.subplots()

# disables axes
ax.axis('off')

plt.title(f"{name} Sort")

# initialise bar plots
bars = ax.bar(range(len(array)), array)

ani = animation.FuncAnimation(fig, animate, fargs=bars, frames=sort, interval=1,
                              repeat=False)


# saves animation to gif
#writer = animation.PillowWriter(fps=25)
#ani.save(f'media/{name}.gif', writer=writer)

plt.show()
