# Array Manipulation

def array_manipulation(n, queries):
    """Return the integer maximum value in the finished array."""

    # Initiate list of 0s
    l = [0] * (n + 1)

    # Loop through query, increment at start index and decrement at end index
    for query in queries:
        a, b, k = query
        l[a - 1] += k
        l[b] -= k

    max_value = a = 0

    # Loop through final list and find max value
    for i in l:
       a += i

       if max_value < a:
            max_value = a

    return max_value


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = array_manipulation(n, queries)
    print("Max value:", result)
