import re
import copy

def solution(expression):
    answer = 0
    # 만들 수 있는 모든 순서
    orders = ['*+-', '*-+', '+*-', '+-*', '-*+', '-+*']

    # 입력에 포함된 모든 숫자를 리스트로 만든다
    nums = re.findall('\d+', expression)
    nums = list(map(int, nums))

    # 입력에 포함된 모든 연산자를 리스트로 만든다
    exp = re.findall('\*|\+|\-', expression)

    for order in orders:
        temp_nums = copy.deepcopy(nums)
        temp_exp = copy.deepcopy(exp)

        # 새로운 순서로 시도할 때마다
        # 처음 입력된 숫자 및 연산자로 초기화한다
        for i in order:
            while i in temp_exp:
                idx = temp_exp.index(i)
                temp_exp.pop(idx)

                if i == '*':
                    temp_ = temp_nums.pop(idx) * temp_nums.pop(idx)
                elif i == '-':
                    temp_ = temp_nums.pop(idx) - temp_nums.pop(idx)
                else:
                    temp_ = temp_nums.pop(idx) + temp_nums.pop(idx)

                temp_nums.insert(idx, temp_)

                # 숫자가 하나 밖에 남지 않았다면
                if(len(temp_nums) == 1):
                    answer = max(abs(temp_nums[0]), answer)
    return answer

'''
만약 수식에 괄호연산자도 있다면, 괄호 연산자를 추가해서 그 부분만 재귀함수를 돌려 값을 return
'''