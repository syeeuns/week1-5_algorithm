import sys
read = sys.stdin.readline

n = int(read())
homework = []
due_dates = []
for i in range(n):
    homework.append(list(map(int, read().split())))
    due_dates.append(homework[i][0])
homework.sort(key=lambda x: -x[1])

date = [0] * (max(due_dates)+1)
for one in homework:
    due = one[0]
    score = one[1]
    for i in range(due, 0, -1):
        if date[i] == 0:
            date[i] = score
            break

print(sum(date))