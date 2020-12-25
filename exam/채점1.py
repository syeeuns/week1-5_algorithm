## 쿼드트리

import sys
r = sys.stdin.readline

###########     입력     ###########

n = int(r())
tree = [list(map(int, list(r().strip()))) for _ in range(n)]


####################################

def color_check(arr, start, end):
    start_color = arr[start[0]][start[1]]
    color_match = True
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            if start_color == arr[i][j]:
                continue
            else:
                color_match = False
                return color_match
    return color_match


def q_tree(arr, start, end, final):
    if color_check(arr, start, end) == False:

        if end[0] - start[0] == 1:
            print('(', end='')
            for i in range(start[0], end[0] + 1):
                for j in range(start[1], end[1] + 1):
                    print(arr[i][j], end='')
            print(')', end='')
        else:
            f_start = start
            f_end = [(start[0] + end[0]) // 2, (start[1] + end[1]) // 2]
            s_start = [start[0], (start[1] + end[1]) // 2 + 1]
            s_end = [(start[0] + end[0]) // 2, end[1]]
            t_start = [(start[0] + end[0]) // 2 + 1, start[1]]
            t_end = [end[0], (start[1] + end[1]) // 2]
            ft_start = [(start[0] + end[0]) // 2 + 1, (start[1] + end[1]) // 2 + 1]
            ft_end = end
            print('(', end='')
            q_tree(arr, f_start, f_end, ft_end)
            q_tree(arr, s_start, s_end, ft_end)
            q_tree(arr, t_start, t_end, ft_end)
            q_tree(arr, ft_start, ft_end, ft_end)
            print(')', end='')
    else:
        color = arr[start[0]][start[1]]
        print(color, end='')


############실행#############

q_tree(tree, [0, 0], [n - 1, n - 1], [n - 1, n - 1])
