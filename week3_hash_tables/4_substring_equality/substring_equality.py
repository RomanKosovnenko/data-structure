# python3

import random
import sys

class Solver:
    def __init__(self, s):
        self.s = s
        self.len_s = len(s)
        self.m1 = (10**9) + 7
        self.m2 = (10**9) + 9
        self.x = random.randint(1, 10**9)
        self.h1 = self.compute_h(self.m1)
        self.h2 = self.compute_h(self.m2)

    def compute_h(self, m):
        h = [0]*(self.len_s+1)
        for i in range(1, self.len_s+1):
            h[i] = (self.x * h[i-1] + ord(self.s[i-1])) % m
        return h
    
    def hash_val(self, h, m, start, length):
        y = pow(self.x, length, m)
        return (h[start + length] - y * h[start]) % m

    def ask(self, a, b, l):
        a_hash1 = self.hash_val(self.h1, self.m1, a, l)
        a_hash2 = self.hash_val(self.h2, self.m2, a, l)
        b_hash1 = self.hash_val(self.h1, self.m1, b, l)
        b_hash2 = self.hash_val(self.h2, self.m2, b, l)
        return a_hash1 == b_hash1 and a_hash2 == b_hash2

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print("Yes" if solver.ask(a, b, l) else "No")
