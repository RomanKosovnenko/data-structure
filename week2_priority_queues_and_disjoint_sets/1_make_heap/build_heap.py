# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    n = len(data)
    last_non_leaf_node = (n//2) - 1
    for i in range(last_non_leaf_node, -1, -1):
        swaps.extend(heapify(data, n, i))
    return swaps

def heapify(arr, n, i):
    swaps = []
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    smallest = i
    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child
    if right_child < n and arr[right_child] < arr[smallest]:
        smallest = right_child
    if smallest != i:
        swaps = [(i, smallest)]
        arr[i], arr[smallest] = arr[smallest], arr[i]
        swaps.extend(heapify(arr, n, smallest))
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
