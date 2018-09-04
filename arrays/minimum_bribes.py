# New Year Chaos Problem

def minimum_bribes(queue):
    """Returns the minimum number of bribes people in a queue accepted."""
    
    # Variable to keep track of bribes
    bribes = 0

    # Check if queue is too chaotic
    for i in queue:
        index = queue.index(i)
        if i - index > 3:
            return "Too chaotic"

    # Use a bubble sort to find number of bribes
    for i in range(len(queue) - 1):
        for j in range(len(queue) - 1 - i):
            if queue[j] > queue[j + 1]:
                queue[j], queue[j + 1] = queue[j + 1], queue[j]
                bribes += 1
    
    return bribes


def read_input():
    # Number of test cases
    t = int(input())
    results = []

    for _ in range(t):

        # Number of people
        _ = int(input())
        # Final State of queue
        q = list(map(int, input().rstrip().split()))

        # Add bribe counts to results array
        results.append(minimum_bribes(q))

    # Print results
    for result in results:
        print(result)


if __name__ == '__main__':
    read_input()