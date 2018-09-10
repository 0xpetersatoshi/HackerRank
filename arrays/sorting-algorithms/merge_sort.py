# Merge Sort Algorithm

def merge_sort(arr):
    """Uses merge sort algorithm to sort an unsorted array."""

    if len(arr) > 1:

        mid = len(arr) // 2
        L = arr[ :mid]
        R = arr[mid: ]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0      
        while i < len(L) and j < len(R):

            if L[i] < R[j]:
                arr[k] = L[i]
                i = i + 1

            else:

                arr[k] = R[j]
                j = j + 1

            k = k + 1

        while i < len(L):

            arr[k] = L[i]
            i = i + 1
            k = k + 1

        while j < len(R):

            arr[k] = R[j]
            j = j + 1
            k = k + 1

    return arr


if __name__ == '__main__':
    
    arr = [54,26,93,17,77,31,44,55,20]
    sorted_arr = merge_sort(arr)
    print(sorted_arr)