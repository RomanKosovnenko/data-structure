# python3

from collections import deque
import sys

m = 10**9 + 7
x = 263

def compute_hash(s, prime, x):
    hash_table = [[] for _ in range(len(s) + 1)]
    hash_table[0] = 0
    for i in range(1, len(s) + 1):
        hash_table[i] = (hash_table[i - 1] * x + ord(s[i - 1])) % prime
    return hash_table

def calculate_hash(hash_table, prime, x, start, length):
    y = pow(x, length, prime)
    return (hash_table[start + length] - y * hash_table[start]) % prime

def check(a_start, length, p_len, k, h1, h2):
    stack = deque()
    stack.append((a_start, 0, length, 1))
    stack.append((a_start+length, length, p_len-length, 1))
    count = 0
    temp = 2
    C = 0
    while stack:
        a, b, L, n = stack.popleft()
        u1 = calculate_hash(h1, m, x, a, L)
        v1 = calculate_hash(h2, m, x, b, L)
        if temp != n:
            count = C
        if u1 != v1:
            count += 1
            if L > 1:
                stack.append((a, b, L//2, n+1))
                stack.append((a + L//2, b + L//2, L - L//2, n+1))
            else:
                C += 1
        if count > k:
            return False
        temp = n
    return count <= k

def solve(k, text, pattern):
    h1 = compute_hash(text, m, x)
    h2 = compute_hash(pattern, m, x)
    return [
        i
        for i in range(len(t) - len(p) + 1)
        if check(i, len(p) // 2, len(p), k, h1, h2)
    ]

for line in sys.stdin.readlines():
    k, t, p = line.split()
    ans = solve(int(k), t, p)
    print(len(ans), *ans)
