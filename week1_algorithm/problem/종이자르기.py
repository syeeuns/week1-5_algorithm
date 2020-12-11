width, height = map(int, input().split())
n = int(input())
horizon = []
vertical = []
for i in range(n):
    direction, number = map(int, input().split())
    if direction == 0:
        horizon.append(number)
    else:
        vertical.append(number)

horizon.append(0)
horizon.append(height)
vertical.append(0)
vertical.append(width)

horizon.sort()
vertical.sort()

diff1 = 0
for i in range(1,len(horizon)):
    if diff1 < (horizon[i] - horizon[i-1]):
        diff1 = horizon[i] - horizon[i-1]

diff2 = 0
for i in range(1, len(vertical)):
    if diff2 < (vertical[i] - vertical[i-1]):
        diff2 = vertical[i] - vertical[i-1]

print(diff1*diff2)