import sys


def input():
    return sys.stdin.readline().rstrip()


N, K = map(int, input().split())

students = [[0] * 6, [0] * 6]

num_rooms = 0

for _ in range(N):
    s, g = map(int, input().split())
    students[s][g - 1] += 1
for s in range(2):
    for g in range(6):
        if students[s][g]:
            num_rooms += (students[s][g] + K - 1) // K
print(num_rooms)
