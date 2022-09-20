import sys


def input():
    return sys.stdin.readline().rstrip()


# 1.if문 여러번 쓰기
A, B, C = map(int, input().split())
if A < B < C:
    print(A, B, C)
elif A < C < B:
    print(A, C, B)
elif B < A < C:
    print(B, A, C)
elif B < C < A:
    print(B, C, A)
elif C < A < B:
    print(C, A, B)
elif C < B < A:
    print(C, B, A)

# 2.리스트 정렬
number_list = list(map(int, input().split()))
number_list.sort()
print(*number_list)
