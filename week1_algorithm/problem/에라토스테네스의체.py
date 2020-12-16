import time
import math
start = time.time()

n = 1000
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    for j in range(i+1, n+1):
        if j % i == 0:
            array[j] = False

for i in range(2, n+1):
    if array[i]:
        print(i)

end = time.time()
print(end-start)