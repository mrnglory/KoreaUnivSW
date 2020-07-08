'''
문제의 목적: 반드시 k개의 숫자를 제거해서 큰 숫자를 만들어냄
숫자의 대소를 결정하는 데에 가장 큰 영향을 끼치는 것은 맨 앞 숫자
제거 했을 때 반드시 그 앞에 있는 숫자부터 다시 검사
'''
def solution(number, k):
    i = 0
    # 마지막까지 갔을 때 더이상 지울 수 있는 문자가 없으므로 존재하는 조건
    while i < len(number) - 1 and k > 0:
        if number[i] < number[i + 1]:   # i번째 숫자보다 i + 1번째 숫자가 크다
            number = number[:i] + number[i + 1:]    # i번째 숫자를 제거한다
            if i != 0:  # 숫자가 제거 되었다면 비교 위치를 앞으로 당긴다
                i -= 1
            k -= 1
        else:   # 숫자가 제거되지 않았다면 비교 위치를 증가시킨다
            i += 1
    if k > 0:   # 제거 해야 할 숫자가 남았다면 뒷부분 숫자를 제거한다
        return number[:k]
    return number

