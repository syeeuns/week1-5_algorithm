import time

# 소수 판별
total = int(input())
start = time.time()

flag = 0
for i in range(2, total):
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    else:
        print(i)

end = time.time()
print(end-start)