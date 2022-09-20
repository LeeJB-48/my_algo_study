import sys


def input():
    return sys.stdin.readline().rstrip()


a, b, c = [int(input()) for _ in range(3)]
prod = a * b * c
num_count = [0] * 10
for char in str(prod):
    num_count[int(char)] += 1
print(*num_count, sep='\n')
