import sys
n = int(sys.stdin.readline().rstrip())

words = set()
for _ in range(n):
    words.add(sys.stdin.readline().rstrip())

words_list = list(words)

# 내 풀이
# arr = [[] for _ in range(51)]
#
# for i in range(len(words_list)):
#     arr[len(words_list[i])].append(words_list[i])
#
# result = []
# for i in range(1, 51):
#     if arr[i]:
#         arr[i] = sorted(arr[i])
#         result += arr[i]
#
# for one in result:
#     print(one)

words_list.sort()
words_list.sort(key=lambda x:len(x))
print('\n'.join(words_list))
