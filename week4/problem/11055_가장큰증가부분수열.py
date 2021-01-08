# dp[i] : i를 마지막 원소로 하는 증가부분 합
import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))
dp = arr[:]
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))

# dp 초기값을 0으로 두면 틀린다 왜?
# dp[j]가 가장 작은 값을 갖는 경우, 갱신이 안돼서 초깃값+arr[i]가 되버림
# (숫자만 세는 문제인 11053에서도 초기값 0으로 안두고 1로 두지 같은 이유로)
# dp 초기값을 arr과 똑같이 둬야함
# 근데 dp = arr 하면 deepcopy돼서 둘이 아예 똑같아지고, dp를 바꾸면 arr도 바뀜
# dp = arr[:] 해야함