import time
import sys

queen = int(sys.stdin.readline().rstrip())
start_time = time.time()

pos = [0] * queen
flag = [False] * queen
flag_right = [False] *(2*queen-1)
flag_left = [False] * (2*queen-1)
cnt = 0

# def put():
#     for i in range(queen):
#         for j in range(queen):
#             print('X' if pos[j]==i else 'O', end=' ')
#         print('')
#     print('')


def set(n, queen):
    for j in range(queen):
        if not flag[j] and not flag_right[n+j] and not flag_left[(queen-1)-n+j]:
            pos[n] = j
            if n == queen-1:
                # put()
                global cnt
                cnt += 1
            else:
                flag[j] = True
                flag_right[n + j] = True
                flag_left[(queen-1) - n + j] = True
                set(n+1, queen)
                flag[j] = False
                flag_right[n + j] = False
                flag_left[(queen-1)- n + j] = False


set(0, queen)
print(cnt)
end_time = time.time()
print(end_time-start_time)