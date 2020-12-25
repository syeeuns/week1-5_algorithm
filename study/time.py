import time
start_time = time.time()

sum = 0
for i in range(10000000):
    sum += i

print(sum)

end_time = time.time()
print(end_time - start_time)

# 파이썬은 1초에 약 천만번의 연산을 할 수 있다
