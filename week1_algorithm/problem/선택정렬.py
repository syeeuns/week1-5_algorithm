arr = [6,3,7,2,0,9,1,5,4,8]
n = len(arr)
# 선택정렬
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[min_index] > arr[j]:
#             arr[min_index], arr[j] = arr[j], arr[min_index]

# 삽입정렬
# for i in range(1, len(arr)):
#     for j in range(i, 0, -1):
#         if arr[j] < arr[j-1]:
#             arr[j], arr[j-1] = arr[j-1], arr[j]
#         else: break

# 버블정렬
for j in range(n):
    for i in range(n-1, j, -1):
        if arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]

print(arr)