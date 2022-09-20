import sys


def input():
    return sys.stdin.readline().rstrip()


for _ in range(3):
    yoot = list(map(int, input().split()))
    sum_yoot = sum(yoot)
    if sum_yoot == 3:
        print('A')
    elif sum_yoot == 2:
        print('B')
    elif sum_yoot == 1:
        print('C')
    elif sum_yoot == 0:
        print('D')
    else:
        print('E')
