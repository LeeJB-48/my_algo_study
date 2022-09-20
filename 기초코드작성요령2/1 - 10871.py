import sys


def input():
    return sys.stdin.readline().rstrip()


N, X = map(int, input().split())
A = list(map(int, input().split()))
for num in A:
    print(num, end=' ') if num < X else None
