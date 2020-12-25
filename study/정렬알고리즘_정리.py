import time
import heapq
start = time.time()
a = [3,5,7,9,0,1,6,8,2,4,3,5,7,8,2,4,6,8,0,2,1,3,4,56,7,9,9,3,2,2,34,5,56,7,8,432,56743,213,2]
# a = [1,8,7,4,5,2,6,3,9]
# def bubbleSort(arr):
#     n = len(arr)
#     cnt =0
#
#     for i in range(n-1):
#         for j in range(n-1, i, -1):
#             if arr[j] < arr[j-1]:
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#
#                 cnt += 1
#
#     print(cnt)
#
# bubbleSort(a)

# def shakerSort(arr):
#     left = 0
#     right = len(arr) - 1
#     last = right
#
#     while left < right:
#         for j in range(right, left, -1):
#             if arr[j-1] > arr[j]:
#                 arr[j-1], arr[j] = arr[j], arr[j-1]
#                 last = j
#         left = last
#
#         for j in range(left, right):
#             if arr[j+1] < arr[j]:
#                 arr[j+1], arr[j] = arr[j], arr[j+1]
#                 last = j
#         right = last
#
# shakerSort(a)

# def selectionSort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         min = i
#         for j in range(i+1, n):
#             if a[min] > a[j]:
#                min = j
#         a[i], a[min] = a[min], a[i]
#
#
# selectionSort(a)

# def countingSort(arr):
#     n = len(arr)
#     counting = [0] * (max(arr)+1)
#     result = []
#     for i in range(n):
#         counting[arr[i]] += 1
#
#     for i in range(max(arr)+1):
#         if counting[i] == 0:
#             continue
#         for j in range(counting[i]):
#             result.append(i)
#
#     return result
#
#
#
# print(countingSort(a))

# def insertSort(arr):
#     n = len(a)
#     for i in range(1,n):
#         j = i
#         temp = a[j]
#         while j > 0 and a[j-1] > temp:
#             a[j] = a[j-1]
#             j -= 1
#         a[j] = temp
#
# insertSort(a)

# def quickSort(arr, left, right):
#     n = len(arr)
#     pl = left
#     pr = right
#     pivot = arr[(left+right)//2]
#
#     while pl <= pr:
#         while a[pl] < pivot: pl+=1
#         while a[pr] > pivot: pr -=1
#         if pl <= pr:
#             a[pl], a[pr] = a[pr], a[pl]
#             pl += 1
#             pr -= 1
#
#     if left < pr:
#         quickSort(arr, left, pr)
#     if right > pl:
#         quickSort(arr, pl, right)
#
# quickSort(a, 0, len(a)-1)

# def mergeSort(arr):
#     def _mergeSort(arr, left, right):
#         if left < right:
#             center = (left+right)//2

#             _mergeSort(arr, left, center)
#             _mergeSort(arr, center+1, right)
#
#             p=j=0
#             i=k=left
#
#             # buff에 앞부분 대입
#             while i <= center:
#                 buff[p] = a[i]
#                 p += 1
#                 i += 1
#
#             # a 뒷부분이랑 buff 병합한거 a에 대입
#             while i <= right and j < p:
#                 if buff[j] <= a[i]:
#                     a[k] = buff[j]
#                     j += 1
#                 else:
#                     a[k] = a[i]
#                     i += 1
#                 k += 1
#
#             while j < p:
#                 a[k] = buff[j]
#                 k += 1
#                 j += 1
#
#     n = len(arr)
#     buff = [None] * n
#     _mergeSort(arr, 0, n-1)
#     del buff
#
# mergeSort(a)


# def heap_sort(arr):
#     heap = []
#     for i in arr:
#         heapq.heappush(heap, i)
#     for i in range(len(arr)):
#         arr[i] = heapq.heappop(heap)
#
# heap_sort(a)

# def heap_sort(arr):
#     def down_heap(arr, left, right):



print(a)

end = time.time()
print(f'time:{end-start}')
# BB : 0.00018787384033203125   O(n^2)
# shaker : :0.00017309188842773438   O(n^2)
# selection : 0.0001418590545654297   O(n^2)
# counting : time:0.004161834716796875
# insert : 0.00010800361633300781   O(n^2)
# quick : 8.416175842285156e-05   O(nlogn)
# merge : 0.0002238750457763672   O(nlogn)
# heap(heapq 라이브러리) : 6.198883056640625e-05   O(nlogn)
