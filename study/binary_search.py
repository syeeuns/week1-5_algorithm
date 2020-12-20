# def binary_search(a, key):
#     pl = 0
#     pr = len(a) - 1
#
#     while True:
#         # 종료조건 : 찾거나, pl이 pr보다 커지거나
#         pc = (pl + pr) // 2
#
#         if a[pc] == key:
#             return pc
#
#         elif a[pc] < key:
#             pl = pc + 1
#
#         elif a[pc] > key:
#             pr = pc - 1
#
#         if pl > pr:
#             break
#     return -1

# 재귀로 구현
def binary_search(a, key, start, end):
    if start > end:
        return None

    center = (start+end) // 2
    if a[center] == key:
        return center
    elif a[center] < key:
        return binary_search(a, key, center+1, end)
    elif a[center] > key:
        return binary_search(a, key, start, center - 1)
    else:
        return -1


a = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(a, 8, 0, len(a)-1))
