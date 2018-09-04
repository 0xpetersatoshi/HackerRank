# Hourglass Problem

import random

arr = [[random.randint(-9, 9) for i in range(6)] for j in range(6)]

def max_hourglass_sum(arr):
    """Return the max hourglass sum."""

    # Define variable to catch max sum
    max_sum = -54

    # Range over array
    for i in range(len(arr)):
        # Range over inner array
        for j in range(len(arr[i])):
            # Create conditions to prevent IndexError
            if (i + 2 < 6) and (j + 2 < 6):
            
                # Sum numbers in hourglass
                total = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] \
                + arr[i + 1][j + 1] + arr[i + 2][j]+ arr[i + 2][j + 1] \
                + arr[i + 2][j + 2]

                # Find max sum
                max_sum = max(max_sum, total)

    return max_sum

if __name__ == "__main__":
    # Calculate sums
    print(max_hourglass_sum(arr))