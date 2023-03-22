# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        heights = [0] * self.n
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                if heights[i] != 0:
                    height += heights[i]
                    break
                height += 1
                i = self.parent[i]
            heights[vertex] = height
            maxHeight = max(maxHeight, height)
        return maxHeight;

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
