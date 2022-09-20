import sys


def input():
    return sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    sys.stdout.write(f"{A + B}\n")
