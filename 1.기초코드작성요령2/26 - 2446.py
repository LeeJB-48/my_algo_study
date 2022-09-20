import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
for i in range(1, 2 * N):
    index = N - abs(N - i)
    print(" " * (index - 1) + "*" * (2 * N - 2 * index + 1))
