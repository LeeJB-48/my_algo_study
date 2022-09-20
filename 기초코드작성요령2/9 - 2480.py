import sys


def input():
    return sys.stdin.readline().rstrip()


three_dice = list(map(int, input().split()))
three_dice.sort()
if three_dice[0] == three_dice[2]:
    print(10000 + three_dice[0] * 1000)
elif three_dice[0] == three_dice[1] or three_dice[1] == three_dice[2]:
    print(1000 + three_dice[1] * 100)
else:
    print(three_dice[2] * 100)
