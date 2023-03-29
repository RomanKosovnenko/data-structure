#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def inOrder(tree):
    stack = []
    result = []
    curr = 0
    while stack or curr != -1:
        if curr != -1:
            root = tree[curr]
            stack.append(root)
            curr = root[1]
        else:
            root = stack.pop()
            result.append(root[0])
            curr = root[2]
    return result


def IsBinarySearchTree(tree):
    order = inOrder(tree)
    for i in range(len(tree)-1):
      if ((tree[i][1]) != -1 and tree[tree[i][1]][0] >= tree[i][0]) or (order[i] > order[i + 1]):
            return False
    return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if nodes == 0 or IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
