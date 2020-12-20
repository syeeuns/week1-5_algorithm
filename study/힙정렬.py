import heapq



def heapsort(arr):
    h = []
    result = []
    for one in arr:
        heapq.heappush(h, (-one, one))
    for i in range(len(h)):
        result.append(heapq.heappop(h)[1])
    return result

a = [5,7,9,2,4,3,6,8,10,1]
print(heapsort(a))