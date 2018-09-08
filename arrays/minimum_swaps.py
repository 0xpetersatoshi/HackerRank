# Minimum Swaps 2

def minimum_swaps(arr):
    """Returns the minimum number of swaps to re-oder array in ascending order."""
    
    # Create dict to hold index position and
    # Create a sorted array variable
    index_of = {value: index for index, value in enumerate(arr)}
    sorted_arr = sorted(arr)

    swaps = 0
    for i in reversed(sorted_arr):

        # Find index of i in original array
        arr_index = index_of[i]

        # Find sorted index
        sorted_index = sorted_arr.index(i)

        if arr_index != sorted_index:
            
            # Perform swap if indexes don't match
            arr[arr_index], arr[sorted_index] = arr[sorted_index], arr[arr_index]
            
            # Increment swaps variable
            swaps += 1

            # Update to reflect new index positions    
            index_of.update( {i: sorted_index} )
            index_of.update( {arr[arr_index]: arr_index} )

    return swaps


arr = [2, 3, 4, 1, 5]

if __name__ == "__main__":
    swaps = minimum_swaps(arr)
    print(swaps)