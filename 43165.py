# numbers에 있는 숫자들을 이용해서
# target을 만드는 경우의 수를 세는 함수
# fibonacci 함수 재귀호출 방법과 비슷한 맥락
# 문제 내용이랑 접근 방식은 이해가 되는데 코드는 알다가도 모르겠음

def solution(numbers, target):
    # not numbers => len(numbers) == 0
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])