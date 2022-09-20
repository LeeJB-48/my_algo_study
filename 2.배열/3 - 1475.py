import math
import sys


def input():
    return sys.stdin.readline().rstrip()


N = input()
plastic_num_count = [0] * 9
for num in N:
    tmp_num = int(num)
    if tmp_num == 9:
        plastic_num_count[6] += 1
    else:
        plastic_num_count[tmp_num] += 1
plastic_num_count[6] = math.ceil(plastic_num_count[6] / 2)
print(max(plastic_num_count))
