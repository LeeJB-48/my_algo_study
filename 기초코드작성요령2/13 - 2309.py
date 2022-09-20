import sys


def input():
    return sys.stdin.readline().rstrip()


nanjangs = [int(input()) for _ in range(9)]
sum_nanjangs = sum(nanjangs)

for i in range(9):
    for j in range(i + 1, 9):
        if sum_nanjangs - nanjangs[i] - nanjangs[j] == 100:
            real_nanjangs = sorted([nanjangs[t] for t in range(9) if t != i and t != j])
for nanjang in real_nanjangs:
    print(nanjang)
