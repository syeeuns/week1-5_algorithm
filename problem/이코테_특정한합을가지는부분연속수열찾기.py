import time
start_time = time.time()

a = [1,2,3,2,5]
m = 5
n = len(a)

cnt = 0
partial_sum = 0
end = 0

# 동빈나 코드
# for start in range(n):
#     while partial_sum < m and end < n:
#         partial_sum += a[end]
#         end += 1
#     if partial_sum == m:
#         cnt += 1
#     partial_sum -= a[start]

# 내 코드 -> 더 빠름
cnt = 0
start = 0
end = 0

partial_sum = 0
while end <= len(a) and start < len(a):
    if a[start] == a[end]:
        partial_sum = a[start]
    else:
        partial_sum = sum(a[start:end+1])

    if partial_sum == m:
        cnt += 1
        start += 1
    elif partial_sum < m:
        end += 1
    elif partial_sum > m:
        start += 1

end_time = time.time()
print(cnt)
print(end_time - start_time)





