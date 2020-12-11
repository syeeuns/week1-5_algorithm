pa = 0
pb = 0

str_a = input()
str_b = input()

if len(str_a) < len(str_b):
    str_a, str_b = str_b, str_a

while pa != len(str_a) and pb != len(str_b):
    if str_a[pa] == str_b[pb]:
        pa += 1
        pb += 1
    else:
        pa = pa - pb + 1
        pb = 0

print(pa-pb+1)