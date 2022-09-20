import sys


def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################

# 1.일반적인 풀이(속도 고려 X)
A, B = map(int, input().split())
if A > B:
    A, B = B, A
print(max(B - A - 1, 0))
for i in range(A + 1, B):
    print(i, end=" ")

# 2. 속도 up 메모리 사용량 up
A, B = map(int, input().split())
if A > B:
    A, B = B, A
print(max(B - A - 1, 0))
ans = " ".join(list(map(str, range(A + 1, B))))
print(ans)
