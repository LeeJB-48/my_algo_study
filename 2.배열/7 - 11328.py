import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())

for _ in range(N):
    arr1 = [0] * 26
    arr2 = [0] * 26
    impossible = False
    word1, word2 = input().split()
    for char in word1:
        arr1[ord(char) - 97] += 1
    for char in word2:
        arr2[ord(char) - 97] += 1
    if arr1 == arr2:
        print("Possible")
    else:
        print("Impossible")
