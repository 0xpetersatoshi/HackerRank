# New Year Chaos Problem
import random

def minimum_bribes(queue):
    """Returns the minimum number of bribes people in a queue accepted."""

    for index, i in enumerate(queue):

        if (i - index) > 3:
            return "Too chaotic"

    n = len(queue)
    swap = 0
    swapped = True
    j = 0

    while swapped:
        
        j += 1
        swapped = False

        for i in range(n - j):
            if queue[i] > queue[i + 1]:

                queue[i], queue[i + 1] = queue[i + 1], queue[i]
                swap += 1
                swapped = True

        print(swap) 
        
    return swap


arr = [random.randint(0, 9) for x in range(1000)]

if __name__ == '__main__':

    print(arr)
    arr = minimum_bribes(arr)
    print(arr)