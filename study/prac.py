a = [3,5,7,9,0,1,6,8,2,4,3,5,7,8,2,4,6,8,0,2,1,3,4,56,7,9,9,3,2,2,34,5,56,7,8,432,56743,213,2]

# def mergeSort(arr):
#     def _mergeSort(arr, left, right):
#         if left < right:
#             center = (left+right)//2
#
#             _mergeSort(arr, left, center)
#             _mergeSort(arr, center+1, right)
#
#             i = left #원래 배열 훑기
#             j = 0 #buff훑기
#             k = left # 새 배열 저장
#             p = 0 #buff저장
#
#             # 원래 배열 앞부분 buff에 저장
#             while i <= center:
#                 buff[p] = a[i]
#                 i+= 1
#                 p+= 1
#
#             # 원래 배열 뒷 부분과 buff 비교해가며 원래 배열에 담기
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
#                 j+=1
#                 k+=1
#
#
#     n = len(arr)
#     buff = [None] * n
#     _mergeSort(arr, 0, n-1)
#     del buff
#
#
# mergeSort(a)




print(a)