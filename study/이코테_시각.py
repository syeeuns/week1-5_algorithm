n = int(input())

cnt = 0

for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            # 책 풀이
            if '3' in str(hour)+str(minute)+str(second):
                cnt += 1
            #  내 풀이
            # if hour % 10 == 3 or hour // 10 == 3:
            #     cnt += 1
            # elif minute % 10 == 3 or minute // 10 == 3:
            #     cnt += 1
            # elif second % 10 == 3 or second // 10 == 3:
            #     cnt += 1


print(cnt)