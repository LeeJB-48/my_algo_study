import sys


def input():
    return sys.stdin.readline().rstrip()


arr1 = [0] * 26
arr2 = [0] * 26
count = 0
for char in input():
    arr1[ord(char) - 97] += 1
for char in input():
    arr2[ord(char) - 97] += 1
for i in range(26):
    count += abs(arr1[i] - arr2[i])
print(count)
