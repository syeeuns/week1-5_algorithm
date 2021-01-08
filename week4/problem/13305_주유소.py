import sys
read = sys.stdin.readline

n = int(read())
dist = list(map(int, read().split()))
oil = list(map(int, read().split()))
i = 0
price = 0
while i < n-1:
    for j in range(i+1, n):
        if oil[i] > oil[j]:
            index = j
            break
        index = j # 못찾으면 마지막 인덱스 반환
    price += oil[i] * (sum(dist[i:index]))
    i = index


print(price)