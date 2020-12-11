n = int(input())
numbers = list(map(int, input().split()))

count = 0
for one in numbers:
    if one == 1:
        continue
    else:
        for i in range(2, one):
            if one % i == 0:
                break
        else:
            count += 1

print(count)

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31