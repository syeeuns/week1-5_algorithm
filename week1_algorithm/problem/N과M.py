# 라이브러리 이용
# from itertools import permutations
#
# n, m = map(int, input().split())
# numbers = [i for i in range(1, n+1)]
# result = list(permutations(numbers, m))
#
# for one in result:
#     for i in range(len(one)):
#         print(one[i], end=' ')
#     print()

# 재귀
n, m = map(int, input().split())
check = [False] * (n+1)
ans = [0] * m

def recursive(index, n, m):
    if index == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return
    for i in range(1, n+1):
        if check[i]:
            continue
        else:
            check[i] = True
            ans[index] = i
            recursive(index+1, n, m)
            check[i] = False

recursive(0, n, m)