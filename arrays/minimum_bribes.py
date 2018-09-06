# New Year Chaos Problem
import time
import random


# def merge_sort(A):
#     """Use a merge sort algorithm to sort the array and find the number of bribes."""

#     # bribes = 0

#     print("Splitting:", A)
#     if len(A) > 1:
#         mid = len(A) // 2
#         L = A[ :mid]
#         R = A[mid: ]

#         merge_sort(L)
#         merge_sort(R)

#         i = j = k = 0      
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 A[k] = L[i]
#                 i = i + 1
#                 # bribes += 1
#             else:
#                 A[k] = R[j]
#                 j = j + 1
#                 # bribes += 1
#             k = k + 1

#         while i < len(L):
#             A[k] = L[i]
#             i = i + 1
#             k = k + 1

#         while j < len(R):
#             A[k] = R[j]
#             j = j + 1
#             k = k + 1
#     print("Merging ", A)


# def merge(A, first, middle, last):
#     """Use a merge sort algorithm to sort the array and find the number of bribes."""

#     L = A[first:middle]
#     R = A[middle:last + 1]
#     L.append(9999999999)
#     R.append(9999999999)
#     i = j = 0

#     for k in range(first, last + 1):
#         if L[i] <= R[j]:
#             A[k] = L[i]
#             i += 1
#         else:
#             A[k] = R[j]
#             j += 1


# def merge_sort2(A, first, last):
#     print("Splitting:", A)
#     if first < last:
#         middle = (first + last) // 2
#         merge_sort2(A, first, middle)
#         merge_sort2(A, middle + 1, last)
#         merge(A, first, middle, last)


# def merge_sort(A):
#     merge_sort2(A, 0, len(A) - 1)


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


# def read_input():
#     # Number of test cases
#     t = int(input())
#     results = []

#     for _ in range(t):

#         # Number of people
#         _ = int(input())
#         # Final State of queue
#         q = list(map(int, input().rstrip().split()))

#         # Add bribe counts to results array
#         results.append(minimum_bribes(q))

#     # Print results
#     for result in results:
#         print(result)

arr = [random.randint(0, 9) for x in range(100000)]

if __name__ == '__main__':
    # read_input()
    start_time = time.time()
    print(arr)
    # merge_sort(arr)
    arr = minimum_bribes(arr)
    print(arr)
    print(time.time() - start_time)