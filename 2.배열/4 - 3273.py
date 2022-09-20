import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
nums = list(map(int, input().split()))
x = int(input())
arr = [0] * 2000001
cnt = 0
for num in nums:
    if arr[x - num]:
        cnt += 1
    arr[num] = 1
print(cnt)
