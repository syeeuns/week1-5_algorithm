s = input()

alphabet = []

sum = 0
for i in range(len(s)):
    # if s[i] == '0' or s[i] == '1' or s[i] == '2' or s[i] == '3' or s[i] == '4' or s[i] == '5' or s[i] == '6' or s[i] == '7' or s[i] == '8' or s[i] == '9':
    if s[i].isdigit():
        sum += int(s[i])

    else:
        alphabet.append(s[i])

alphabet.sort()
print(''.join(alphabet) + str(sum))
