# python3

from collections import deque

def max_sliding_window_naive(sequence, m):
    dq = deque()

    for i in range(m):
        while dq and sequence[i] >= sequence[dq[-1]]:
            dq.pop()
        dq.append(i)

    maximums = []
    for i in range(m, len(sequence)):
        maximums.append(sequence[dq[0]])

        while dq and dq[0] <= (i - m):
            dq.popleft()
        
        while dq and sequence[i] >= sequence[dq[-1]]:
            dq.pop()
        
        dq.append(i)
    maximums.append(sequence[dq[0]])
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

