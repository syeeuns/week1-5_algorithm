import sys

n, m = map(int, sys.stdin.readline().split())
trees = sorted(list(map(int, sys.stdin.readline().split())))

start = 0
end = max(trees)


while start <= end:
    center = (start + end) // 2
    remain = 0
    for one in trees:
        if one > center:
            remain += one - center

# 대체 왜 여기 등호붙으면 틀리고 떼면 맞는가 !
    ## 목표는 적절한 center값을 찾는것이다.
    ## end 는 종료 시 start - 1 이 됨이 자명하다.
    ## 그렇다면, 종료시 center값은  avg( end (=start-1), start ) 인데
    ## 연속된 두 값의 몫은 둘중 작은 값이므로.. end로 출력해도 답이 나온다.
    ## 하지만, print를 { end => (start+ end) // 2 } 로하는 것이 더 명확할 수 있다
    if remain == m:
        answer = center
        break
    elif remain < m:
        end = center - 1
    else: # 이게 만족 조건 이니까 이쪽에 등호 붙이는게 맞고, 이거 answer 저장하는 것이 맞음
        answer = center # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 answer에 저장
        start = center + 1

print(answer)


