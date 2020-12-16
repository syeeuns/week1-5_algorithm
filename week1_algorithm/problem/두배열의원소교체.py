n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

# for i in range(k):
#     temp_a = min(a)
#     temp_b = max(b)
#     a.remove(temp_a)
#     a.append(temp_b)
#     b.remove(temp_b)
#     b.append(temp_a)
#
# print(sum(a))

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else: break

print(sum(a))