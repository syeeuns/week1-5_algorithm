# voca의 길이만큼씩 비교를 해준다
# 단어 일치하면 그 수만큼 넘어감
# 불일치하면 하나씩 넘겨줌
# 마지막에 단어 길이 넘어가면 break
import sys
read = sys.stdin.readline

document = read().rstrip()
voca = read().rstrip()
cnt = 0
i = 0
document_size = len(document)
voca_size = len(voca)
while i <= document_size - voca_size:
    if document[i:i + voca_size] == voca: # 단어랑 같으면 점프
        i += voca_size
        cnt += 1
    else:
        i += 1


print(cnt)

# 끝까지 고려안할거니까 rstrip ㄴㄴ 
