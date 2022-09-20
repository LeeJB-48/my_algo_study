import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
calls = list(map(int, input().split()))
young_price = 0
min_price = 0

for call in calls:
    young_share = call // 30 + 1
    min_share = call // 60 + 1

    young_price += young_share * 10
    min_price += min_share * 15

if young_price == min_price:
    print("Y M", young_price)
elif young_price < min_price:
    print("Y", young_price)
else:
    print("M", min_price)
