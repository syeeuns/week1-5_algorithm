import math
import time
start = time.time()
# 1000까지 소수 구하기 (1. 제곱근까지만 2. 에라토스테네스의 체) -> 1이 더 빠름    
#1. time:0.0008859634399414062
# prime = [2,]
#
# for i in range(3, 1001, 2):
#     flag = True
#     for j in range(2, int(i**0.5)+1):
#         if i % j == 0:
#             flag = False
#             break
#     if flag:
#         prime.append(i)

#2. time:0.0011818408966064453
prime = [2,]
result = [i for i in range(3,1001)]

for one in result:
    flag = True
    for i in range(2, int(one**0.5)+1):
        if one % i == 0:
            flag = False
            break
    if flag:
        prime.append(one)

end = time.time()
print(prime)
print(f'time:{end-start}')
