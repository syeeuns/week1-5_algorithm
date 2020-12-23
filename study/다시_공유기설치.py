import sys
read = sys.stdin.readline

n, c = map(int, read().rstrip().split())
home = []
for i in range(n):
    home.append(int(read().rstrip()))
home.sort()

# 간격으로 이분탐색하여 공유기 수를 찾는다
start = 1
end = home[-1] - home[0]
answer = 0
while start <= end:
    router = 1 # 첫번째에 무조건 1개 설치하고 시작
    front = home[0]
    mid = (start + end) // 2
    for i in range(1, len(home)):
        if (home[i] - front) >= mid:
            router += 1
            front = home[i]

    if router >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)

