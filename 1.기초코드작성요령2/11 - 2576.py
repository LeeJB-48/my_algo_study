import sys


def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################

odd_sum = 0
min_odd_num = 100  # 주어지는 값의 최대보다 1 크게
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        odd_sum += num
        min_odd_num = min(min_odd_num, num)
if odd_sum:
    print(odd_sum, min_odd_num, sep='\n')
else:
    print(-1)
