import sys


def input():
    return sys.stdin.readline().rstrip()


# 1.이중 포문
N = int(input())

for i in range(1, N + 1):
    for j in range(N - i):
        print(" ", end="")
    print("*" * i)

# 2.단일 포문
N = int(input())

for i in range(1, N + 1):
    print(" " * (N - i) + "*" * i)

# 3.한번에
N = int(input())
print("\n".join([" " * (N - i) + "*" * i for i in range(1, N + 1)]))
