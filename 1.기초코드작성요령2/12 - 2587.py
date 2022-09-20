import sys


def input():
    return sys.stdin.readline().rstrip()


num_list = []
for _ in range(5):
    num = int(input())
    num_list.append(num)
num_list.sort()
average = sum(num_list) // 5
median = num_list[2]
print(average, median, sep='\n')
