import sys
read = sys.stdin.readline

n, k = map(int, read().split())
coins = []
for i in range(n):
    coins.append(int(read()))

coins.sort(reverse=True)
answer = 0
for coin in coins:
    answer += k // coin
    k %= coin

print(answer)