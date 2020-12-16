n, row, col = map(int, input().split())

square = 0
answer = 0
def sum(n, row, col):
    global answer
    global square
    if n == 1:
        if row == 0 and col == 0:
            answer += 0
        elif row == 0 and col == 1:
            answer += 1
        elif row == 1 and col == 0:
            answer += 2
        elif row == 1 and row == 1:
            answer += 3
        return

    else:
        line = 2 ** (n - 1)
        if row < line and col < line:
            square = 0
            answer += 0
            sum(n-1, row, col)
        elif row < line and col >= line:
            square = 1
            answer += 2**(2*n-2)
            sum(n-1, row, col-line)
        elif row >= line and col < line:
            square = 2
            answer += 2*(2 **(2*n-2))
            sum(n-1, row-line, col)
        elif row >= line and col >= line:
            square = 3
            answer += 3 * (2 ** (2*n-2))
            sum(n-1, row-line, col-line)


sum(n, row, col)
print(answer)



