# 시작한 쇠막대기 갯수 | 잘린 쇠막대기 조각의 갯수
#         0                    0
#         1                    3
#         2                    6
#         3                    7
#         2                   10
#         3                   11
#         2                   13
#         1                   14
#         0                   15
#         1                   16
#         0                   17

def solution(arrangement):
    answer = 0
    sticks = 0
    laser_to_r = arrangement.replace('()', 'L')
    for i in laser_to_r:
        if i == '(':
            sticks += 1
        elif i == ')':
            sticks -= 1
            answer += 1
        else:
            answer += sticks
    return answer