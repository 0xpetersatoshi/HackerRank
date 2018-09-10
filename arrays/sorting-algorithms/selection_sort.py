# Selection Sort Algorithm

def selection_sort(arr):
    """Uses selection sort algorithm to sort an unsorted array."""
    
    for fillslot in range(len(arr) - 1, 0, -1):

       position_of_max = 0

       for location in range(1, fillslot + 1):

           if arr[location] > arr[position_of_max]:
               position_of_max = location

       arr[fillslot], arr[position_of_max] = arr[position_of_max], arr[fillslot]

    return arr


if __name__ == '__main__':

    arr = [54,26,93,17,77,31,44,55,20]
    sorted_arr = selection_sort(arr)
    print(sorted_arr)