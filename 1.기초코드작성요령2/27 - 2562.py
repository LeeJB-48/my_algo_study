import sys


def input():
    return sys.stdin.readline().rstrip()


nums = [int(input()) for _ in range(9)]

max_num = 0
max_index = 0
for i in range(9):
    if nums[i] > max_num:
        max_index = i
        max_num = nums[i]
print(max_num)
print(max_index + 1)
