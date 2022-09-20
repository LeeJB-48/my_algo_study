import sys


def input():
    return sys.stdin.readline().rstrip()


S = input()
arr = [0] * 26
for char in S:
    arr[ord(char) - 97] += 1
print(*arr)
