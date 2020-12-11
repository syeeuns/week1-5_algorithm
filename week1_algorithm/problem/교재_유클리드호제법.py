# 유클리드 호제법
# 재귀 ㄴㄴ
# def euclid(a, b):
#     while True:
#         temp = b
#         b = a % b
#         a = temp
#         if b == 0:
#             return a

# 재귀
def euclid(a, b):
    if b == 0:
        return a
    return euclid(b, a%b)

a, b = map(int, input().split())
if a < b:
    a, b = b, a
print(euclid(a, b))
