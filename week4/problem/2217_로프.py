# 로프가 버틸수 있는 중량 배열 w[]
# 오름차순 sort했을 때, w[N-a] * a 기 됨은 자명하다
import sys
read = sys.stdin.readline

n = int(read())
w = []
for i in range(n):
    w.append(int(read()))
w.sort()
result = w[n-1] * 1
for i in range(2, n+1):
    result = max(result, w[n-i] * i)
print(result)
