import sys
read = sys.stdin.readline

n, k = map(int, read().split())
arr = [i for i in range(1, n+1)]
idx = k - 1
new = [str(arr.pop(k-1))]
while len(new) < n:
    idx += k - 1
    if idx > len(arr) - 1:
        idx %= len(arr)
    new.append(str(arr.pop(idx)))
print('<'+', '.join(new)+'>')